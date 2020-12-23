import copy, time
startTime= time.time()

firstList= []
posA= None
posB= None

def readFile(fileName):
    global posA, posB
    inputDict= {
        'rules':{},
        'input':[]
    }
    category= 'rules'
    with open(fileName) as inputfile:
        for line in inputfile:
            if len(line.strip()) < 1:
                category= 'input'
            elif category == 'rules':
                rules= line.strip().split(':')
                inputDict[category][rules[0]]= []
                splitedRules= rules[1].split(' ')
                rule= []
                for r in splitedRules:
                    r= r.replace('\"','')
                    if len(r) < 1:
                        None
                    # elif r in ['a','b']:
                    #     inputDict[category][rules[0]]= r
                    elif r == '|':
                        inputDict[category][rules[0]].append(rule)
                        rule= []
                    else:
                        rule.append(r)
                    if r == 'a':
                        posA= rules[0]
                    elif r == 'b':
                        posB= rules[0]
                try:
                    inputDict[category][rules[0]].append(rule)
                except:
                    None
            else:
                inputDict[category].append(line.strip())
    return inputDict

def printFirstList():
    for rule in firstList:
        print(rule)

def updateFirstListOneStep():
    newFirstList= [[]]
    for rule in firstList:
        tmpFirstList= [[]]
        # print("---0")
        for ruleNbr in rule:
            # print("---1")
            # print("ruleNbr: {}".format(ruleNbr))
            tmpList= []
            if ruleNbr in ['a','b']:
                for newRule in tmpFirstList:
                    # print("---2 0")
                    tmpList.append(newRule + [ruleNbr])
            else:
                # print(input['rules'][ruleNbr])
                # print("first:{} * rule:{} = {}".format(len(newFirstList),len(input['rules'][ruleNbr]),len(newFirstList)*len(input['rules'][ruleNbr])))

                for newRule in tmpFirstList:
                    # print("---2 1")
                    for extRule in input['rules'][ruleNbr]:
                        # print("---3")
                        # newRule + extRule
                        # print("newRule: {}".format(newRule))
                        tmpList.append(newRule + extRule)

            # print("tmp: {}".format(tmpList))
            tmpFirstList= tmpList
        newFirstList+= tmpFirstList
    # print("newFirstList: {}".format(newFirstList))
    return newFirstList

def removeEmptyFromList():
    emptyArrInList= True
    while emptyArrInList:
        emptyArrInList= False
        if [] in firstList:
            firstList.remove([])
            emptyArrInList= True

def convertArrsToStrings(rules):
    for rulePos in range(len(rules)):
        newStr= ""
        for char in rules[rulePos]:
            newStr+= char
        rules[rulePos]= newStr
    return rules

validCounter= 0
def removeFromInput(validList):
    global validCounter
    oldInput= input['input']
    for stringToVerify in oldInput:
        if stringToVerify in validList:
            validCounter+= 1
            input['input'].remove(stringToVerify)
        elif len(stringToVerify) < shortestRule:
            print('----')
            input['input'].remove(stringToVerify)
    # for stringInList in input['input']:
        # print(stringInList)
    print("Valid: {}".format(validCounter))
    print("Input: {}".format(len(input['input'])))

shortestRule= 0
def removeInvalidFromRules():
    global shortestRule
    shortestRule= 10000
    # print(len(firstList))
    nbrRemoved= 0
    for rule in firstList.copy():
        if len(rule) < shortestRule:
            print(rule)
            shortestRule= len(rule)
        # print("r0: {}".format(rule))
        validRule= True
        tmpRule= ""
        for char in rule:
            if char not in ['a','b']:
                # print("Numbers in rule")
                validRule= False
                break
            tmpRule+= char
        if validRule:
            print("r1: {}".format(rule))
            ruleNeeded= False
            for row in input['input']:
                # print("tmp: {}\nrow: {}".format(tmpRule,row))
                if tmpRule == row:
                    ruleNeeded= True
                    break
            if not ruleNeeded:
                # print("Removing: {}".format(rule))
                nbrRemoved+= 1
                firstList.remove(rule)
        else:
            ruleNeeded= False
            for row in input['input']:
                if tmpRule == row[:len(tmpRule)]:
                    ruleNeeded= True
                    break
            if not ruleNeeded:
                # print("Removing: {}".format(rule))
                nbrRemoved+= 1
                firstList.remove(rule)
                print("Removed: {}".format(nbrRemoved),end='',flush=True)
    print("Removed: {}".format(nbrRemoved))

def populateA():
    print(input['rules']['14'])
    for ruleNbr in input['rules']:
        # print("{}: {}".format(ruleNbr,input['rules'][ruleNbr]))
        i= 0
        for rule in input['rules'][ruleNbr]:
            newRule= []
            for nbr in rule:
                if nbr == posA:
                    newRule.append('a')
                elif nbr == posB:
                    newRule.append('b')
                else:
                    newRule.append(nbr)
            input['rules'][ruleNbr][i]= newRule
            i+= 1
        # print("{}: {}".format(ruleNbr,input['rules'][ruleNbr]))
    del input['rules'][posA]
    del input['rules'][posB]

def populateAB():
    replaceNbrs= []
    for ruleNbr in input['rules']:
        if len(input['rules'][ruleNbr]) == 1:
            isAlpha= True
            for nbr in input['rules'][ruleNbr][0]:
                if nbr not in ['a','b']:
                    isAlpha= False
            if isAlpha:
                replaceNbrs.append(ruleNbr)
    print(replaceNbrs)
    for ruleNbr in input['rules']:
        i= 0
        for rule in input['rules'][ruleNbr]:
            newRule= []
            for nbr in rule:
                if nbr in replaceNbrs:
                    newRule+= input['rules'][nbr][0]
                    # print("newRule0: {}".format(newRule))
                else:
                    newRule.append(nbr)
                    # print("newRule1: {}".format(newRule))
            # print("newRule: {}".format(newRule))
            input['rules'][ruleNbr][i]= newRule
            i+= 1
    for nbr in replaceNbrs:
        del input['rules'][nbr]



# 8: 42 | 42 8
# 11: 42 31 | 42 11 31
# input= readFile('input')
input= readFile('exampleInput2')
print(input['rules'])
print(posA)
print(posB)
populateAB()
print(input['rules'])
populateAB()
print(input['rules'])
populateAB()
print(input['rules'])
# print(input['rules']['8'])
input['rules']['8']= [['42'],['42','8']]
input['rules']['11']= [['42','31'],['42','11','31']]
# print(input)
firstList= input['rules']['0']
# print("---=== FL ===---\n{}".format(firstList))
# firstList= updateFirstListOneStep()
# print("---=== FL ===---\n{}".format(firstList))
# firstList= updateFirstListOneStep()
# print("---=== FL ===---\n{}".format(firstList))
# firstList= updateFirstListOneStep()

continueUpdate= True
i= 0
while continueUpdate and i < 4:
    # continueUpdate= False
    print("firstList: {}".format(len(firstList)))
    firstList= updateFirstListOneStep()
    print("firstList: {}".format(len(firstList)))
    removeEmptyFromList()
    # printFirstList()
    # print()
    listOfValidRules= convertArrsToStrings(copy.deepcopy(firstList))
    removeInvalidFromRules()
    removeFromInput(listOfValidRules)
    # removeInvalidFromRules()
    print("shortestRule: {}".format(shortestRule))
    print("firstList: {}".format(len(firstList)))
    print()
    # printFirstList()
    # print()
    # for rules in firstList:
    #     for rule in rules:
    #         if rule not in ['a','b']:
    #             continueUpdate= True
    i+= 1


# for rules in firstList:
#     if '8' in rules:
#         rules.remove('8')
#     if '11' in rules:
#         rules.remove('11')
    # print(rules)
# print("---=== FL ===---\n{}".format(firstList))
# removeEmptyFromList()
# print("---=== FL ===---\n{}".format(firstList))
# listOfValidRules= convertArrsToStrings(copy.deepcopy(firstList))
# print("---=== FL ===---\n{}".format(firstList))
# removeValidFromInput(listOfValidRules)
# validCounter= 0
# for stringToVerify in input['input']:
#     if stringToVerify in firstList:
#         validCounter+= 1
print(len(firstList))
print(validCounter)

endTime= time.time()
print("execution time: {}".format(endTime-startTime))

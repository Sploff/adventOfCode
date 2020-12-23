import copy, time
startTime= time.time()

firstList= []

def readFile(fileName):
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
                try:
                    inputDict[category][rules[0]].append(rule)
                except:
                    None
            else:
                inputDict[category].append(line.strip())
    return inputDict

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

def removeEmpty():
    emptyArrInList= True
    while emptyArrInList:
        emptyArrInList= False
        firstList.remove([])
        if [] in firstList:
            emptyArrInList= True

def convertArrToString():
    for rulePos in range(len(firstList)):
        newStr= ""
        for char in firstList[rulePos]:
            newStr+= char
        firstList[rulePos]= newStr


input= readFile('input')
# input= readFile('exampleInput')
# print(input)
firstList= input['rules']['0']
# print("---=== FL ===---\n{}".format(firstList))
# firstList= updateFirstListOneStep()
# print("---=== FL ===---\n{}".format(firstList))
# firstList= updateFirstListOneStep()
# print("---=== FL ===---\n{}".format(firstList))
# firstList= updateFirstListOneStep()

continueUpdate= True
while continueUpdate:
    continueUpdate= False
    firstList= updateFirstListOneStep()
    for rules in firstList:
        for rule in rules:
            if rule not in ['a','b']:
                continueUpdate= True

# print("---=== FL ===---\n{}".format(firstList))
removeEmpty()
# print("---=== FL ===---\n{}".format(firstList))
convertArrToString()
# print("---=== FL ===---\n{}".format(firstList))

validCounter= 0
for stringToVerify in input['input']:
    if stringToVerify in firstList:
        validCounter+= 1
print(validCounter)

endTime= time.time()
print("execution time: {}".format(endTime-startTime))

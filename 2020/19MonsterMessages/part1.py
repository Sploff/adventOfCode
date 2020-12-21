import copy, time
startTime= time.time()
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

# input= readFile('input')
input= readFile('exampleInput')

def prettyPrint(rules):
    for rule in input['rules']:
        print("{}: {}".format(rule,input['rules'][rule]))

# for rule in input['rules']:
#     print("{}: {}".format(rule,input['rules'][rule]))
# prettyPrint(input['rules'])
# print(input['input'])
#############################
#####   EXAMPLE INPUT   #####
#############################
# 0: [['4', '1', '5']]
# 1: [['2', '3'], ['3', '2']]
# 2: [['4', '4'], ['5', '5']]
# 3: [['4', '5'], ['5', '4']]
# 4: 'a'
# 5: 'b'
# ['ababbb', 'bababa', 'abbbab', 'aaabbb', 'aaaabbb']
#############################
#####   VALID STRINGS   #####
#############################
# aaaabb, aaabab, abbabb, abbbab, aabaab, aabbbb, abaaab, or ababbb
#############################

def test1(arrIn, arrOut):
    # print("in: {}, out: {}".format(arrIn,arrOut))
    for c in arrIn:
        if c in ['a','b']:
            arrOut.append(c)
        else:
            # arrOut.append([])
            oldArrOut= copy.deepcopy(arrOut)
            tmpArr= []
            for rules in input['rules'][c]:
                # print(rules)
                x = test1(rules,oldArrOut)

                print("x: {}".format(x))
                tmpArr+= x
                # print(arrOut)
            # print("tmp: {}".format(tmp))
            # arrOut.append(tmpArr)
            arrOut= tmpArr
    print(arrOut)
    return arrOut

print(test1(['4','2'],[]))

def mergeRules(allRules):
    for ruleNbr in allRules:
        for rules in allRules[ruleNbr]:
            if rules not in ['a','b']:
                i= 0
                for rule in rules:
                    rules[i]= allRules[rule]
                    i+= 1
    return allRules
############################
#####   mergeRules()   #####
############################
# 0: [['a', [[[['a', 'a'], ['b', 'b']], [['a', 'b'], ['b', 'a']]], [[['a', 'b'], ['b', 'a']], [['a', 'a'], ['b', 'b']]]], 'b']]
# 1: [[[['a', 'a'], ['b', 'b']], [['a', 'b'], ['b', 'a']]], [[['a', 'b'], ['b', 'a']], [['a', 'a'], ['b', 'b']]]]
# 2: [['a', 'a'], ['b', 'b']]
# 3: [['a', 'b'], ['b', 'a']]
# 4: a
# 5: b

def mergeRules2(allRules):
    for ruleNbr in allRules:
        for rules in allRules[ruleNbr]:
            if rules not in ['a','b']:
                i= 0
                for rule in rules:
                    newRules= []
                    for r in allRules[rule]:
                        None
                    rules[i]= allRules[rule]
                    i+= 1
    return allRules

def cleanup(allRules):
    for ruleNbr in allRules:
        i= 0
        for rules in allRules[ruleNbr]:
            if rules not in ['a','b']:
                merge= True
                for rule in rules:
                    if rule not in ['a','b']:
                        merge= False
                if merge:
                    # print(rules)
                    mergedRule= ''
                    for rule in rules:
                        mergedRule+= rule
                    # print(mergedRule)
                    rules= mergedRule
                    allRules[ruleNbr][i]= mergedRule
                    # print(rules)
            i+= 1
    # prettyPrint(allRules)
#########################
#####   cleanup()   #####
#########################
# 0: [['a', [[['aa', 'bb'], ['ab', 'ba']], [['ab', 'ba'], ['aa', 'bb']]], 'b']]
# 1: [[['aa', 'bb'], ['ab', 'ba']], [['ab', 'ba'], ['aa', 'bb']]]
# 2: ['aa', 'bb']
# 3: ['ab', 'ba']
# 4: a
# 5: b
#############################
#####   VALID STRINGS   #####
#############################
# aaaabb, aaabab, abbabb, abbbab, aabaab, aabbbb, abaaab, or ababbb
#############################

# 0: [['4', '1', '5']]
# 1: [['2', '3'], ['3', '2']]
# 2: [['4', '4'], ['5', '5']]
# 3: [['4', '5'], ['5', '4']]
# 4: 'a'
# 5: 'b'
def mergeMainRules(allRules):
    print("allRules Before: " + str(allRules['0']))

    newRules= []
    for r in allRules['0']:
        print("r: {}".format(r))
        mainRules= [[]]
        for mainRule in r:
            print("main Before: " + str(mainRules))
            print("mainrule: " + str(mainRule))
            tmpRules= mainRules.copy()
            if mainRule in ['a','b']:
                mainRules= []
                for tmpRule in tmpRules:
                    mainRules.append(tmpRule + rules)
            elif allRules[mainRule] in ['a','b']:
                mainRules= []
                for rule in tmpRules:
                    rule.append(allRules[mainRule])
                    mainRules.append(rule)
            else:
                mainRules= []
                for rules in allRules[mainRule]:
                    for tmpRule in tmpRules:
                        # print(tmpRule)
                        # print(rules)
                        mainRules.append(tmpRule + rules)
            print("main After : {}\n".format(str(mainRules)))
        print(mainRules)
        newRules.append(mainRules)
    print("---" + str(newRules))
    allRules['0']= newRules[0]
    print("allRules After : {}\n".format(str(allRules['0'])))
    oneMoreTime= False
    for checkAB in newRules[0]:
        if checkAB not in ['a','b']:
            oneMoreTime= True
    mergeMainRules(allRules)

def mergeMainRules2(allRules):
    newRules= []
    nbrOneRules= allRules['0']
    # nbrOneRules= [['4', '1', '5']]
    for mainRules in nbrOneRules:
        # mainRules= ['4', '1', '5']
        for mainRule in mainRules:
            # mainRule= '4'
            # mainRule= '1'
            # mainRule= '5'
            if mainRule in ['a','b']:
                None
            else:
                for subRules in allRules[mainRule]:
                    # subRules= ['a']
                    # subRules= ['2', '3']
                    # subRules= ['3', '2']
                    # subRules= ['b']
                    if len(newRules) < 1:
                        newRules.append(subRules)
                    else:
                        tmpRules= []
                        for subRule in subRules:
                            print("subRule: {}".format(subRule))
                            for newRule in newRules:
                                tmpRules.append([])
                                for nr in newRule:
                                    print("nr: {}".format(nr))
                                    tmpRules[-1].append(nr)
                                    print("tmpRule1: {}".format(tmpRules))
                            tmpRules[-1].append(subRule)
                            print("tmpRule2: {}\n".format(tmpRules))
                        newRules= tmpRules
    print(newRules)

def updateSubRule(rules):
    newRule1= []
    newRule2= []
    for rule1 in rules:
        newRule2.append([])
        for rule2 in input['rules'][rule1]:
            newRule2[-1].append(rule2)
            print("rule1: {}, rule2: {}".format(rule1,rule2))
        print("")
    print(newRule2)
    for nr2 in newRule2:
        None
    return

def updateSubRule2(rules):
    newRule= []
    for rule in rules:
        print(rule)
        if rule in ['a','b']:
            newRule.append(rule)
        else:
            newRule.append(updateSubRule2(input['rules'][rule]))
    return newRule

# updateSubRule(['2','3'])
# print(updateSubRule2([['2','3'],['3','2']))

# mergedRules= mergeRules(input['rules'])
# cleanup(mergedRules)
# prettyPrint(mergedRules)
# mergeMainRules2(input['rules'])
# mergeMainRules2(input['rules'])



endTime= time.time()
print("execution time: {}".format(endTime-startTime))

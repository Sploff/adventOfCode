import copy, time
startTime= time.time()
def readFile(fileName):
    inputArray= []
    with open(fileName) as inputfile:
        for line in inputfile:
            inputArray.append(line.strip().replace(" ",""))
    return inputArray

input= readFile('input')
# input= readFile('exampleInput')

def subCalculation(subExpression):
    transExpression= []
    lastNbr= ""
    for c in subExpression:
        if c not in ['+','*']:
            lastNbr+= c
        else:
            transExpression.append(lastNbr)
            transExpression.append(c)
            lastNbr= ""
    transExpression.append(lastNbr)
    newExp= transExpression.copy()
    additionFound= True
    p= False
    while additionFound:
        lastNbr= 0
        lastOperator= ' '
        transExpression= newExp.copy()
        newExp= []
        additionFound= False
        for c in transExpression:
            if additionFound:
                newExp.append(c)
            elif c == '+':
                lastOperator= c
            elif c == '*':
                lastOperator= c
                newExp.append(lastNbr)
                newExp.append(c)
            else:
                if lastOperator == '+':
                    additionFound= True
                    newExp.append(str(lastNbr + int(c)))
                lastNbr= int(c)


    answer= 1
    for c in transExpression:
        if c != '*':
            answer*= int(c)
    return answer

def calculate(expression):
    while True:
        lastRightBracket= 0
        for i in range(len(expression),0,-1):
            c= expression[i-1]
            if c == ')':
                lastRightBracket= i
            elif c == '(':
                expression= expression[:i-1] + str(subCalculation(expression[i:lastRightBracket-1])) + expression[lastRightBracket:]
                break
        if not lastRightBracket:
            return subCalculation(expression)

sum= 0
for expression in input:
    # print("{} = {}".format(expression, calculate(expression)))
    sum+= calculate(expression)
print(sum)

endTime= time.time()
print("execution time: {}".format(endTime-startTime))

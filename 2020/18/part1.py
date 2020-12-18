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
    # print("subExp: " + subExpression)
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
    # print(trans)
    answer= 0
    lastOperator= '+'
    for c in transExpression:
        if c in ['+','*']:
            lastOperator= c
        else:
            if lastOperator == '+':
                answer+= int(c)
            else:
                answer*= int(c)
    return answer

def calculate(expression):
    # print("\nexp: " + expression)
    while True:
        lastRightBracket= 0
        for i in range(len(expression),0,-1):
            c= expression[i-1]
            if c == ')':
                lastRightBracket= i
            elif c == '(':
                # print(expression[i-1:lastRightBracket])
                expression= expression[:i-1] + str(subCalculation(expression[i:lastRightBracket-1])) + expression[lastRightBracket:]
                # print(expression)
                break
        if not lastRightBracket:
            return subCalculation(expression)

# print("{} = {}".format(input[0], subCalculation(input[0])))
sum= 0
for expression in input:
    # print("{} = {}".format(expression, calculate(expression)))
    sum+= calculate(expression)
print(sum)

endTime= time.time()
print("execution time: {}".format(endTime-startTime))

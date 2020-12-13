import time
startTime= time.time()

def readFile(fileName):
    inputArray= []
    with open(fileName) as inputfile:
        for line in inputfile:
            inputArray.append(int(line.strip()))
    return inputArray

input= sorted(readFile('input'))
lenHalf= [25,50,75]
# input= sorted(readFile('exampleInput'))
# lenHalf= 9
# input= sorted(readFile('miniExample'))
# lenHalf=5

input1= input[0:25]
input2= input[25:50]
input3= input[50:77]
input4= input[77:]
print("input: {}, input1: {}, input2: {}, input3: {}, input4: {}".format(len(input),len(input1),len(input2),len(input3),len(input4)))
print("input: {}, input1: {}, input2: {}, input3: {}, input4: {}".format(input,input1,input2,input3,input4))

allCombinations= []
def magic(restList):
    # print(restList)
    global allCombinations
    lastJolts= [0,0]
    for x in restList:
        # print(restList)
        if x-lastJolts[0] <= 3 and lastJolts[1] > 0:
            # print(1)
            # print(restList)
            tmpList= restList.copy()
            # print(tmpList)
            tmpList.remove(lastJolts[1])
            if tmpList not in allCombinations:
                allCombinations.append(tmpList)
                # print(len(allCombinations))
                magic(tmpList)
        lastJolts[0]= lastJolts[1]
        lastJolts[1]= x


allCombinations= []
magic(input1)
nbr1= len(allCombinations) +1
allCombinations= []
magic(input2)
nbr2= len(allCombinations) +1
allCombinations= []
magic(input3)
nbr3= len(allCombinations) +1
allCombinations= []
magic(input4)
nbr4= len(allCombinations) +1
print(nbr1)
print(nbr2)
print(nbr3)
print(nbr4)
print(nbr1*nbr2*nbr3*nbr4)

# print(allCombinations)
# validCombinations= []
# for comb in allCombinations:
#     # print(comb)
#     comb= sorted(comb)
#     # print(comb)
#     # print(validCombinations)
#     if comb not in validCombinations:
#         validCombinations.append(comb)

# print("counter: {}".format(len(validCombinations)+1))
print("counter: {}".format(len(allCombinations)+1))

endTime= time.time()
print("execution time: {} (input length: {})".format(endTime-startTime, len(input)))

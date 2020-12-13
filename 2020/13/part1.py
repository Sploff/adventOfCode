import copy, time
startTime= time.time()
def readFile(fileName):
    inputArray= []
    with open(fileName) as inputfile:
        for line in inputfile:
            inputArray.append(line.strip().split(","))
    return inputArray

input= readFile('input')
# input= readFile('exampleInput')

# print(input)
bestBus= 0
bestTime= 10000000
for bus in input[1]:
    if bus != "x":
        rest= int(input[0][0])%int(bus)
        diff= int(bus)-rest
        if diff < bestTime:
            bestTime= diff
            bestBus= int(bus)
        # print(bus + ": " + str(int(bus)-rest))
print(bestBus*bestTime)

endTime= time.time()
print("execution time: {}".format(endTime-startTime))

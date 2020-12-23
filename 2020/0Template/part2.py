import copy, time
startTime= time.time()

def readFile(fileName):
    inputArray= []
    with open(fileName) as inputfile:
        for line in inputfile:
            inputArray.append(line.strip())
    return inputArray


endTime= time.time()
print("execution time: {}".format(endTime-startTime))

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
# input= [[],['17','x','13','19']]
# input= [[],['67','7','59','61']]
# input= [[],['67','x','7','59','61']]
# input= [[],['67','7','x','59','61']]
# input= [[],['1789','37','47','1889']]
# input= [[],['1','2','3','5']]



found= False
startTimestamp= 0
i= 0
intInput=[]
for bus in input[1]:
    if bus != 'x':
        intInput.append(int(bus))
intInput.sort()
print(intInput)
maxInput= intInput[-1]
maxInput2= intInput[-2]
maxInput3= intInput[-3]
maxPos= input[1].index(str(maxInput))
maxPos2= input[1].index(str(maxInput2))
maxPos3= input[1].index(str(maxInput3))
print(maxInput)
print(maxPos)
print(maxInput2)
print(maxPos2)
print(maxInput3)
print(maxPos3)
j= 0
k= 0
while not found:
    # if startTimestamp > 3500:
    #     break
    # if startTimestamp % 1000000 == 0:
    #     print(startTimestamp / 1000000)
    found= True
    timestamp= startTimestamp
    # if timestamp > 0:
    #     print(str(timestamp))
    for bus in input[1]:
        if bus != "x":
            rest= timestamp%int(bus)
            if rest != 0:
                # print(str(startTimestamp+maxPos) + " % " + input[1][maxPos] +" = "+ str((startTimestamp+maxPos) % int(input[1][maxPos])))
                if j < 4:
                    if (startTimestamp+maxPos) % int(input[1][maxPos]) == 0:
                        i+= 1
                        if (
                        (startTimestamp+maxPos2) % int(input[1][maxPos2]) == 0 and
                        (startTimestamp+maxPos3) % int(input[1][maxPos3]) == 0
                        ):
                            # print("i: " + str(i) + ", j: " + str(j))
                            if j > 1:
                                startTimestamp+= int(input[1][maxPos])*i
                            k= i
                            i= 0
                            j+= 1
                        else:
                            startTimestamp+= int(input[1][maxPos])
                    else:
                        startTimestamp+= int(input[1][0])
                else:
                    startTimestamp+= int(input[1][maxPos])*k
                found= False
                break
        timestamp+= 1

print(startTimestamp)

endTime= time.time()
print("execution time: {}".format(endTime-startTime))

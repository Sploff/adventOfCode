import copy, time
startTime= time.time()
def readFile(fileName):
    inputArray= []
    with open(fileName) as inputfile:
        for line in inputfile:
            inputArray.append(line.strip().split(" = "))
    return inputArray

input= readFile('input')
# input= readFile('exampleInputPart2')

memory= {}
mask0= None
mask1= None
maskX0= None
maskX1= None
for line in input:
    if line[0] == 'mask':
        mask0= (2**64)-1
        mask1= 0
        maskX0= (2**64)-1
        maskX1= [0]
        i= 35
        for char in line[1]:
            if char == '0':
                mask0-= 2**i
            elif char == '1':
                mask1+= 2**i
            elif char == 'X':
                maskX0-= 2**i
                maskX1.append(2**i)
                for mask in maskX1:
                    newMask= mask | 2**i
                    if newMask not in maskX1:
                        maskX1.append(newMask)
            i-=1
    else:
        mem= int(line[0].replace("]","").split("[")[1])
        for mask in maskX1:
            memory[((mem&maskX0)|mask)|mask1]= int(line[1])
sum= 0
for m in memory:
    sum+= memory[m]
print(sum)

endTime= time.time()
print("execution time: {}".format(endTime-startTime))

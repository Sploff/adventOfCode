import copy, time
startTime= time.time()
def readFile(fileName):
    inputArray= []
    with open(fileName) as inputfile:
        for line in inputfile:
            inputArray.append(line.strip().split(" = "))
    return inputArray

input= readFile('input')
# input= readFile('exampleInput')

print(input)

memory= {}
mask0= None
mask1= None
for line in input:
    if line[0] == 'mask':
        mask0= (2**64)-1
        mask1= 0
        i= 35
        for char in line[1]:
            if char == '0':
                mask0-= 2**i
            elif char == '1':
                mask1+= 2**i
            i-=1
    else:
        memory[line[0]]= int(line[1])
        memory[line[0]]= memory[line[0]] & mask0
        memory[line[0]]= memory[line[0]] | mask1

# print(bin(mask0))
# print(bin(mask1))
print(memory)
sum= 0
for m in memory:
    sum+= memory[m]
print(sum)

endTime= time.time()
print("execution time: {}".format(endTime-startTime))

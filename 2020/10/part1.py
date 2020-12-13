def readFile(fileName):
    inputArray= []
    with open(fileName) as inputfile:
        for line in inputfile:
            inputArray.append(int(line.strip()))
    return inputArray

input= sorted(readFile('input'))
# input= sorted(readFile('exampleInput'))
# input= sorted(readFile('miniExample'))

lastJolt= 0
counter= [0,0,0,0]
for x in input:
    # print("lastJolt: {}, x: {}, diff: {}".format(lastJolt,counter,x-lastJolt))
    counter[x-lastJolt]+=1
    lastJolt= x


print("counter: {}, ans: {}".format(counter, counter[1]*(counter[3]+1)))

import copy, time
startTime= time.time()
def readFile(fileName):
    inputArray= []
    with open(fileName) as inputfile:
        for line in inputfile:
            instr= []
            instr.append(line.strip()[0])
            instr.append(int(line.strip()[1:]))
            inputArray.append(instr)
    return inputArray

input= readFile('input')
# input= readFile('exampleInput')

pos= [0,0] #East, North
deg= 0

for instr in input:
    if instr[0] == 'N':
        pos[1]+= instr[1]
    elif instr[0] == 'S':
        pos[1]-= instr[1]
    elif instr[0] == 'E':
        pos[0]+= instr[1]
    elif instr[0] == 'W':
        pos[0]-= instr[1]
    elif instr[0] == 'L':
        deg-= instr[1]/90
        nbrTurns%= 4
    elif instr[0] == 'R':
        deg+= instr[1]/90
    elif instr[0] == 'F':
        nbrTurns= deg%4
        dir= 'E'
        if nbrTurns == 1:
            dir= 'S'
        elif nbrTurns == 2:
            dir= 'W'
        elif nbrTurns == 3:
            dir= 'N'
        if nbrTurns == -1:
            dir= 'N'
        elif nbrTurns == -2:
            dir= 'W'
        elif nbrTurns == -3:
            dir= 'S'
        input.append([dir,instr[1]])
    # print(instr)
    # print(str(deg) + ", " + str(pos))

print(pos)
print(abs(pos[0])+abs(pos[1]))
# print("counter: {}, ans: {}".format(counter, counter[1]*(counter[3]+1)))


endTime= time.time()
print("execution time: {}".format(endTime-startTime))

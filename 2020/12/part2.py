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
wp= [10,1]
deg= 0

for instr in input:
    if instr[0] == 'N':
        wp[1]+= instr[1]
    elif instr[0] == 'S':
        wp[1]-= instr[1]
    elif instr[0] == 'E':
        wp[0]+= instr[1]
    elif instr[0] == 'W':
        wp[0]-= instr[1]
    elif instr[0] == 'L':
        nbrTurns= (instr[1]/90)%4
        newWp= [0,0]
        if nbrTurns == 1:
            newWp[0]= wp[1] * -1
            newWp[1]= wp[0]
        elif nbrTurns == 2:
            newWp[0]= wp[0] * -1
            newWp[1]= wp[1] * -1
        elif nbrTurns == 3:
            newWp[0]= wp[1]
            newWp[1]= wp[0] * -1
        wp= newWp
    elif instr[0] == 'R':
        nbrTurns= (instr[1]/90)%4
        newWp= [0,0]
        if nbrTurns == 1:
            newWp[0]= wp[1]
            newWp[1]= wp[0] * -1
        elif nbrTurns == 2:
            newWp[0]= wp[0] * -1
            newWp[1]= wp[1] * -1
        elif nbrTurns == 3:
            newWp[0]= wp[1] * -1
            newWp[1]= wp[0]
        wp= newWp
    elif instr[0] == 'F':
        pos[0]+= wp[0]*instr[1]
        pos[1]+= wp[1]*instr[1]
    # print(instr)
    # print(str(deg) + ", " + str(pos))

print(pos)
print(abs(pos[0])+abs(pos[1]))
# print("counter: {}, ans: {}".format(counter, counter[1]*(counter[3]+1)))


endTime= time.time()
print("execution time: {}".format(endTime-startTime))

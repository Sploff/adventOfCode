import copy, time
startTime= time.time()
def readFile(fileName):
    inputArray= []
    with open(fileName) as inputfile:
        for line in inputfile:
            inputArray.append(list(line.strip()))
    return inputArray

input= readFile('input')
# input= readFile('exampleInput')
width= len(input[0])
height= len(input)
max= max([width,height])
# print(max)

def prettyPrint(seatMap):
    for row in seatMap:
        print(row)

def findO(pos, direction, seatMap):
    for i in range(max):
        x= i+1
        # if pos[0] == 1 and pos[1] == 0:
            # print("[{},{}]".format(pos[0]+direction[0]*x,pos[1]+direction[1]*x))
            # print(direction)
        if(
        pos[0]+direction[0]*x < 0 or
        pos[1]+direction[1]*x < 0
        ):
            return False
        try:
            if seatMap[pos[0]+direction[0]*x][pos[1]+direction[1]*x] == 'L':
                return False
            if seatMap[pos[0]+direction[0]*x][pos[1]+direction[1]*x] == 'O':
                return True
        except:
            None
    return False

def updateSeats(seatMap):
    # prettyPrint(seatMap)
    # print(" ")
    nextSeatMap= copy.deepcopy(seatMap)
    prtStr= ""
    for coordY in range(height):
        for coordX in range(width):
            prtStr+= "\n[{},{}]: ".format(coordY,coordX)
            if seatMap[coordY][coordX] in ['L','O']:
                alone= True
                counter= 0
                for x in range(-1,2):
                    for y in range(-1,2):
                        if(
                        not(x == 0 and y == 0) and
                        coordX+x >= 0 and
                        coordY+y >= 0 and
                        coordX+x < width and
                        coordY+y < height):
                            prtStr+= " ({},{}) ".format(y,x)
                            if findO([coordY,coordX],[y,x],seatMap):
                                alone= False
                                counter+= 1
                prtStr+= str(counter)
                if alone:
                    nextSeatMap[coordY][coordX]= 'O'
                # print(counter)
                if counter > 4:
                    nextSeatMap[coordY][coordX]= 'L'
    # print(prtStr)
    return nextSeatMap



oldSeats= input
newSeats= updateSeats(input)
anotherRound= True
counter= 0
i= 0
while(anotherRound):
    i+=1
    counter= 0
    anotherRound= False
    for coordY in range(height):
        for coordX in range(width):
            if(newSeats[coordY][coordX] == 'O'):
                counter+= 1
            if oldSeats[coordY][coordX] != newSeats[coordY][coordX]:
                anotherRound= True
    oldSeats= newSeats
    newSeats= updateSeats(newSeats)

print(counter)
endTime= time.time()
print("execution time: {}".format(endTime-startTime))

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

def prettyPrint(seatMap):
    for row in seatMap:
        print(row)

def updateSeats(seatMap):
    # prettyPrint(seatMap)
    # print(" ")
    width= len(seatMap[0])
    height= len(seatMap)
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
                            if seatMap[coordY+y][coordX+x] == 'O':
                                alone= False
                                counter+= 1
                prtStr+= str(counter)
                if alone:
                    nextSeatMap[coordY][coordX]= 'O'
                # print(counter)
                if counter > 3:
                    nextSeatMap[coordY][coordX]= 'L'
    # print(prtStr)
    anotherRound= False
    counter= 0
    for coordY in range(height):
        for coordX in range(width):
            if(seatMap[coordY][coordX] == 'O'):
                counter+= 1
            if seatMap[coordY][coordX] != nextSeatMap[coordY][coordX]:
                anotherRound= True
        # print(anotherRound)
    if anotherRound:
        # prettyPrint(seatMap)
        updateSeats(nextSeatMap)

    # print(nextSeatMap)
    print(counter)


updateSeats(input)
# print(input)
# print("counter: {}, ans: {}".format(counter, counter[1]*(counter[3]+1)))


endTime= time.time()
print("execution time: {}".format(endTime-startTime))

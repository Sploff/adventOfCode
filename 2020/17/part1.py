import copy, time
startTime= time.time()

def readFile(fileName):
    inputArray= []
    with open(fileName) as inputfile:
        inputArray.append([])
        for line in inputfile:
            inputArray[-1].append([])
            for c in line.strip():
                inputArray[-1][-1].append(c)
                # print(inputArray)
    return inputArray

space= readFile("input")
# space= readFile("exampleInput")

def createNewSpace(space):
    newSpace= []
    for z in range(len(space) + 2):
        # print("z: {}, len(z): {}".format(z,len(space)))
        newSpace.append([])
        for y in range(len(space[0]) + 2):
            # print("y: {}, len(y): {}".format(y,len(space[0])))
            newSpace[z].append([])
            for x in range(len(space[0][0]) + 2):
                # print("x: {}, len(x): {}".format(x,len(space[0][0])))
                newSpace[z][y].append(".")
    return(newSpace)

def expandOldSpace(space):
    expandedSpace= []
    for z in range(len(space) + 2):
        expandedSpace.append([])
        for y in range(len(space[0]) + 2):
            expandedSpace[z].append([])
            for x in range(len(space[0][0]) + 2):
                if(
                z > 0 and
                y > 0 and
                x > 0 and
                z < len(space)+1 and
                y < len(space[0])+1 and
                x < len(space[0][0])+1 and
                space[z-1][y-1][x-1] == "#"
                ):
                    expandedSpace[z][y].append("#")
                else:
                    expandedSpace[z][y].append(".")
    return(expandedSpace)


def populateNewSpace(space):
    zMin= False
    zMax= False
    yMin= False
    yMax= False
    xMin= False
    xMax= False
    near= [-1,0,1]
    nbrCubes= 0
    newSpace= createNewSpace(space)
    space= expandOldSpace(space)
    for z in range(len(newSpace)):
        for y in range(len(newSpace[z])):
            for x in range(len(newSpace[z][y])):
                c= 0
                for dZ in near:
                    for dY in near:
                        for dX in near:
                            try:
                                if dZ == 0 and dY == 0 and dX == 0:
                                    None
                                elif space[z+dZ][y+dY][x+dX] == "#":
                                    c+= 1
                            except:
                                None
                if c == 3:
                    newSpace[z][y][x]= "#"
                elif c == 2 and space[z][y][x] == "#":
                    newSpace[z][y][x]= "#"
                else:
                    newSpace[z][y][x]= "."
                if newSpace[z][y][x] == "#":
                    nbrCubes+= 1
                    if z == 0:
                        zMin= True
                    if y == 0:
                        yMin= True
                    if x == 0:
                        xMin= True
                    if z == len(newSpace)-1:
                        zMax= True
                    if y == len(newSpace[z])-1:
                        yMax= True
                    if x == len(newSpace[z][y])-1:
                        xMax= True
    # cleanSpace(space, zMin, yMin, xMin, zMax, yMax, xMax)
    return newSpace, nbrCubes

# def cleanSpace(space, zMin, yMin, xMin, zMax, yMax, xMax):
#     for z in range(len(space)):
#         for y in range(len(space[z])):
#             for x in range(len(space[z][y])):
#                 if z == 0:
#                     if newSpace[z][y][x] == "#":
#                         None


def prettyPrint(space):
    for z in space:
        for y in z:
            print(y)
        print("\n")


# print(space)
# print(getNewSpace(space))
# prettyPrint(space)
# prettyPrint(expandOldSpace(space))
# prettyPrint(createNewSpace(space))
# prettyPrint(populateNewSpace(space))
# getNewSpace(space)
i= 0
while i < 6:
    space, nbrCubes= populateNewSpace(space)
    print(nbrCubes)
    i+= 1


endTime= time.time()
print("execution time: {}".format(endTime-startTime))

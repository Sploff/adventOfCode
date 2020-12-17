import copy, time
startTime= time.time()

def readFile(fileName):
    inputArray= []
    with open(fileName) as inputfile:
        inputArray.append([])
        for line in inputfile:
            inputArray[-1].append([[]])
            for c in line.strip():
                inputArray[-1][-1][-1].append(c)
                # print(inputArray)
    return inputArray

space= readFile("input")
# space= readFile("exampleInput")

def createNewSpace(space):
    newSpace= []
    for w in range(len(space) + 2):
        newSpace.append([])
        for z in range(len(space[0]) + 2):
            # print("z: {}, len(z): {}".format(z,len(space)))
            newSpace[w].append([])
            for y in range(len(space[0][0]) + 2):
                # print("y: {}, len(y): {}".format(y,len(space[0])))
                newSpace[w][z].append([])
                for x in range(len(space[0][0][0]) + 2):
                    # print("x: {}, len(x): {}".format(x,len(space[0][0])))
                    newSpace[w][z][y].append(".")
    return(newSpace)

def expandOldSpace(space):
    expandedSpace= []
    for w in range(len(space) + 2):
        expandedSpace.append([])
        for z in range(len(space[0]) + 2):
            expandedSpace[w].append([])
            for y in range(len(space[0][0]) + 2):
                expandedSpace[w][z].append([])
                for x in range(len(space[0][0][0]) + 2):
                    if(
                    w > 0 and
                    z > 0 and
                    y > 0 and
                    x > 0 and
                    w < len(space)+1 and
                    z < len(space[0])+1 and
                    y < len(space[0][0])+1 and
                    x < len(space[0][0][0])+1 and
                    space[w-1][z-1][y-1][x-1] == "#"
                    ):
                        expandedSpace[w][z][y].append("#")
                    else:
                        expandedSpace[w][z][y].append(".")
    return(expandedSpace)

nbrCubes= 0
def populateNewSpace(space):
    global nbrCubes
    # zMin= False
    # zMax= False
    # yMin= False
    # yMax= False
    # xMin= False
    # xMax= False
    near= [-1,0,1]
    nbrCubes= 0
    newSpace= createNewSpace(space)
    space= expandOldSpace(space)
    for w in range(len(newSpace)):
        for z in range(len(newSpace[w])):
            for y in range(len(newSpace[w][z])):
                for x in range(len(newSpace[w][z][y])):
                    c= 0
                    for dW in near:
                        for dZ in near:
                            for dY in near:
                                for dX in near:
                                    try:
                                        if dW == 0 and dZ == 0 and dY == 0 and dX == 0:
                                            None
                                        elif space[w+dW][z+dZ][y+dY][x+dX] == "#":
                                            c+= 1
                                    except:
                                        None
                    if c == 3:
                        newSpace[w][z][y][x]= "#"
                    elif c == 2 and space[w][z][y][x] == "#":
                        newSpace[w][z][y][x]= "#"
                    else:
                        newSpace[w][z][y][x]= "."
                    if newSpace[w][z][y][x] == "#":
                        nbrCubes+= 1
    # cleanSpace(space, zMin, yMin, xMin, zMax, yMax, xMax)
    return newSpace

# def cleanSpace(space, zMin, yMin, xMin, zMax, yMax, xMax):
#     for z in range(len(space)):
#         for y in range(len(space[z])):
#             for x in range(len(space[z][y])):
#                 if z == 0:
#                     if newSpace[z][y][x] == "#":
#                         None


def prettyPrint(space):
    for w in space:
        # print("w: "+str(w))
        for z in w:
            for y in z:
                print(y)
            print("\n")
        print("\n")


# print(space)
# print(getNewSpace(space))
# prettyPrint(space)
# # prettyPrint(expandOldSpace(space))
# prettyPrint(createNewSpace(space))
# prettyPrint(populateNewSpace(space))
# getNewSpace(space)
i= 0
while i < 6:
    space= populateNewSpace(space)
    # prettyPrint(space)
    print(nbrCubes)
    i+= 1


endTime= time.time()
print("execution time: {}".format(endTime-startTime))

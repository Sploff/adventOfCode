import copy, time
startTime= time.time()

def readFile(fileName):
    inputArray= []
    with open(fileName) as inputfile:
        for line in inputfile:
            row= list(line.strip())
            instructions= []
            instruction= ''
            while len(row) > 0:
                instruction+= row.pop(0)
                if instruction in ['ne','e','se','sw','w','nw']:
                    instructions.append(instruction)
                    instruction= ''
            inputArray.append(instructions)
    return inputArray

instructionsList= readFile('input')
# instructionsList= readFile('exampleInput')

origo= [0,0]
tileMap= [[1]]

def addLeft():
    for row in tileMap:
        row.insert(0,1)
    origo[0]+= 1

def addRight():
    for row in tileMap:
        row.append(1)

def addTop():
    newTop= []
    for _ in tileMap[0]:
        newTop.append(1)
    tileMap.insert(0,newTop)
    origo[1]+= 1

def addBottom():
    newTop= []
    for _ in tileMap[0]:
        newTop.append(1)
    tileMap.append(newTop)

def printTileMap():
    nbrWhites= 0
    nbrBlacks= 0
    printRow= ''
    x= 0
    y= 0
    for row in tileMap:
        for tile in row:
            if tile > 0:
                nbrWhites+= 1
                if origo == [x,y]:
                    printRow+= '\''
                else:
                    printRow+= 'X'
            else:
                nbrBlacks+= 1
                if origo == [x,y]:
                    printRow+= '.'
                else:
                    printRow+= 'O'
            x+= 1
        y+= 1
        x= 0
        print(printRow)
        printRow= ''
    print("Whites: {}, Blacks: {}".format(nbrWhites,nbrBlacks))

def flipTile(instructions):
    nextPos= None
    extendedMap= True
    i= 0
    while extendedMap and i<2:
        i+= 1
        extendedMap= False
        nextPos= origo.copy()
        for instruction in instructions:
            if instruction == 'ne':
                nextPos[1]-= 1
                nextPos[0]+= 1
            if instruction == 'e':
                nextPos[0]+= 1
            if instruction == 'se':
                nextPos[1]+= 1
            if instruction == 'sw':
                nextPos[1]+= 1
                nextPos[0]-= 1
            if instruction == 'w':
                nextPos[0]-= 1
            if instruction == 'nw':
                nextPos[1]-= 1


        if nextPos[0] < 0:
            for _ in range(nextPos[0]*-1):
                addLeft()
            extendedMap= True
        elif nextPos[0] > len(tileMap[0])-1:
            for _ in range(nextPos[0]-len(tileMap[0])+1):
                addRight()
            extendedMap= True
        if nextPos[1] < 0:
            for _ in range(nextPos[1]*-1):
                addTop()
            extendedMap= True
        elif nextPos[1] > len(tileMap)-1:
            for _ in range(nextPos[1]-len(tileMap)+1):
                addBottom()
            extendedMap= True
    tileMap[nextPos[1]][nextPos[0]]*= -1

for instructions in instructionsList:
    flipTile(instructions)
print()
printTileMap()

def prepareFloor():
    first= False
    first2= False
    last= False
    last2= False
    for row in tileMap:
        if row[0] == -1:
            first= True
        if row[1] == -1:
            first2= True
        if row[-1] == -1:
            last= True
        if row[-2] == -1:
            last2= True
    if -1 in tileMap[0]:
        addTop()
    if -1 in tileMap[1]:
        addTop()
    if -1 in tileMap[-1]:
        addBottom()
    if -1 in tileMap[-2]:
        addBottom()
    if first:
        addLeft()
    if first2:
        addLeft()
    if last:
        addRight()
    if last2:
        addRight()

day= 0
def nextDay():
    global day
    prepareFloor()
    tmpTileMap= copy.deepcopy(tileMap)
    for y in range(1,len(tileMap)-1):
        for x in range(1,len(tileMap[0])-1):
            nbrBlacks= 0
            if tmpTileMap[y-1][x] < 0:
                nbrBlacks+= 1
            if tmpTileMap[y-1][x+1] < 0:
                nbrBlacks+= 1
            if tmpTileMap[y][x-1] < 0:
                nbrBlacks+= 1
            if tmpTileMap[y][x+1] < 0:
                nbrBlacks+= 1
            if tmpTileMap[y+1][x-1] < 0:
                nbrBlacks+= 1
            if tmpTileMap[y+1][x] < 0:
                nbrBlacks+= 1
            if tmpTileMap[y][x] > 0 and nbrBlacks == 2:
                tileMap[y][x]= -1
            elif tmpTileMap[y][x] < 0 and nbrBlacks == 0:
                tileMap[y][x]= 1
            elif tmpTileMap[y][x] < 0 and nbrBlacks > 2:
                tileMap[y][x]= 1
    day+= 1

for _ in range(100):
    nextDay()
    # print(day)
    # printTileMap()

printTileMap()

endTime= time.time()
print("execution time: {}".format(endTime-startTime))

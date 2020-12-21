import copy, time
startTime= time.time()
def readFile(fileName):
    inputDict= {}
    with open(fileName) as inputfile:
        tileNbr= None
        for line in inputfile:
            row= line.strip().replace("Tile ","")
            if ":" in row:
                tileNbr= row.replace(":","")
                inputDict[tileNbr]= {
                    'img':[],
                    'c':0,
                    'n':None,
                    'e':None,
                    's':None,
                    'w':None
                }
            elif len(row) > 0:
                inputDict[tileNbr]['img'].append(row)
    return inputDict

input= readFile('input')
# input= readFile('exampleInput')

def prettyPrint(toPrint):
    for tileNbr in toPrint:
        print("\nTile: {}, c: {}".format(tileNbr,toPrint[tileNbr]['c']))
        for row in toPrint[tileNbr]['img']:
            print(row)


def findMatch(side, blTileNbr):
    # print()
    # print(side +" "+ blTileNbr)
    for tileNbr in input:
        if tileNbr != blTileNbr:
            # print(input[tileNbr]['img'][0])
            # print(input[tileNbr]['img'][-1])
            sides= getSides(tileNbr)
            if(
            side == input[tileNbr]['img'][0] or
            side == input[tileNbr]['img'][0][::-1] or
            side == input[tileNbr]['img'][-1] or
            side == input[tileNbr]['img'][-1][::-1] or
            side == sides[0] or
            side == sides[0][::-1] or
            side == sides[1] or
            side == sides[1][::-1]
            ):
                # print('MATCH!!!! ' + tileNbr)
                return [tileNbr]
    return None

def getSides(tileNbr):
    leftSide= ""
    rightSide= ""
    for row in input[tileNbr]['img']:
        leftSide+= row[0]
        rightSide+= row[-1]
    return [leftSide,rightSide]

def updateTile(tileNbr):
    matchNbr= findMatch(input[tileNbr]['img'][0],tileNbr)
    if matchNbr:
        input[tileNbr]['c']+= 1
        input[tileNbr]['n']= matchNbr
    matchNbr= findMatch(input[tileNbr]['img'][-1],tileNbr)
    if matchNbr:
        input[tileNbr]['c']+= 1
        input[tileNbr]['s']= matchNbr
    sides= getSides(tileNbr)
    matchNbr= findMatch(sides[0],tileNbr)
    if matchNbr:
        input[tileNbr]['c']+= 1
        input[tileNbr]['w']= matchNbr
    matchNbr= findMatch(sides[1],tileNbr)
    if matchNbr:
        input[tileNbr]['c']+= 1
        input[tileNbr]['e']= matchNbr

product= 1
for tileNbr in input:
    updateTile(tileNbr)
    if input[tileNbr]['c'] == 2:
        product*= int(tileNbr)
# updateTile('2473')
print(product)
# prettyPrint(input)

endTime= time.time()
print("execution time: {}".format(endTime-startTime))

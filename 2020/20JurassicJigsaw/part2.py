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
        print("\nTile: {}, c: {}\nn: {}, e: {}, s: {}, w: {}".format(tileNbr,toPrint[tileNbr]['c'],toPrint[tileNbr]['n'],toPrint[tileNbr]['e'],toPrint[tileNbr]['s'],toPrint[tileNbr]['w']))
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
            side == sides['left'] or
            side == sides['left'][::-1] or
            side == sides['right'] or
            side == sides['right'][::-1]
            ):
                # print('MATCH!!!! ' + tileNbr)
                return tileNbr
    return None

def getSides(tileNbr):
    leftSide= ""
    rightSide= ""
    for row in input[tileNbr]['img']:
        leftSide+= row[0]
        rightSide+= row[-1]
    return {'left':leftSide,'right':rightSide}

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
    matchNbr= findMatch(sides['left'],tileNbr)
    if matchNbr:
        input[tileNbr]['c']+= 1
        input[tileNbr]['w']= matchNbr
    matchNbr= findMatch(sides['right'],tileNbr)
    if matchNbr:
        input[tileNbr]['c']+= 1
        input[tileNbr]['e']= matchNbr

def fixToMatch(tileNbr, side, matchSide):
    # print("tileNbr: {}, side: {}, matchSide: {}".format(tileNbr,side,matchSide))
    # tileNbr: 1489, side: w, matchSide: #...##.#.#
    sides= getSides(tileNbr)
    if side == 'w':
        if matchSide == sides['left']:
            None
        elif matchSide == sides['left'][::-1]:
            flip(tileNbr,'v')
        elif matchSide == sides['right']:
            flip(tileNbr,'h')
        elif matchSide == sides['right'][::-1]:
            flip(tileNbr,'v')
            flip(tileNbr,'h')
        elif matchSide == input[tileNbr]['img'][0]:
            rotate(tileNbr,'l')
            flip(tileNbr,'v')
        elif matchSide == input[tileNbr]['img'][0][::-1]:
            rotate(tileNbr,'l')
        elif matchSide == input[tileNbr]['img'][-1]:
            rotate(tileNbr,'r')
        elif matchSide == input[tileNbr]['img'][-1][::-1]:
            rotate(tileNbr,'r')
            flip(tileNbr,'v')
    elif side == 'n':
        if matchSide == input[tileNbr]['img'][0]:
            None
        elif matchSide == input[tileNbr]['img'][0][::-1]:
            flip(tileNbr,'h')
        elif matchSide == input[tileNbr]['img'][-1]:
            flip(tileNbr,'v')
        elif matchSide == input[tileNbr]['img'][-1][::-1]:
            flip(tileNbr,'h')
            flip(tileNbr,'v')
        elif matchSide == sides['left']:
            rotate(tileNbr,'r')
            flip(tileNbr,'h')
        elif matchSide == sides['left'][::-1]:
            rotate(tileNbr,'r')
        elif matchSide == sides['right']:
            rotate(tileNbr,'l')
        elif matchSide == sides['right'][::-1]:
            rotate(tileNbr,'l')
            flip(tileNbr,'h')


def flip(tileNbr, direction):
    newTile= []
    if direction == 'v':
        for row in input[tileNbr]['img'][::-1]:
            newTile.append(row)
        northTile= input[tileNbr]['n']
        input[tileNbr]['n']= input[tileNbr]['s']
        input[tileNbr]['s']= northTile
    else:
        for row in input[tileNbr]['img']:
            newTile.append(row[::-1])
        eastTile= input[tileNbr]['e']
        input[tileNbr]['e']= input[tileNbr]['w']
        input[tileNbr]['w']= eastTile
    input[tileNbr]['img']= newTile

def rotate(tileNbr, direction):
    newTile= []
    if direction == 'l':
        for x in range(len(input[tileNbr]['img'])):
            newTile.append("")
            for row in input[tileNbr]['img']:
                newTile[-1]+= row[x]
        input[tileNbr]['img']= newTile
        n= input[tileNbr]['e']
        e= input[tileNbr]['s']
        s= input[tileNbr]['w']
        w= input[tileNbr]['n']
        flip(tileNbr,'v')
        input[tileNbr]['e']= e
        input[tileNbr]['s']= s
        input[tileNbr]['w']= w
        input[tileNbr]['n']= n
    else:
        for x in range(len(input[tileNbr]['img'])):
            newTile.append("")
            for row in input[tileNbr]['img']:
                newTile[-1]+= row[x]
        input[tileNbr]['img']= newTile
        n= input[tileNbr]['w']
        e= input[tileNbr]['n']
        s= input[tileNbr]['e']
        w= input[tileNbr]['s']
        flip(tileNbr,'h')
        input[tileNbr]['e']= e
        input[tileNbr]['s']= s
        input[tileNbr]['w']= w
        input[tileNbr]['n']= n

def removeBorder(tileNbr):
    newTile= []
    for row in input[tileNbr]['img'][1:-1]:
        newTile.append(row[1:-1])
    input[tileNbr]['img']= newTile

# prettyPrint({'2971':input['2971']})
# print()
# removeBorder('2971')
# prettyPrint({'2971':input['2971']})

topLeftTile= None
for tileNbr in input:
    updateTile(tileNbr)
    # if tileNbr == '2971':
    #     prettyPrint({'2971':input['2971']})
    #     prettyPrint({'1489':input['1489']})
    #     prettyPrint({'1171':input['1171']})
    if(
    not input[tileNbr]['n'] and
    not input[tileNbr]['w']
    ):
        topLeftTile= tileNbr

bigImageTileNbrs= []
nextS= 'first'
tileInFocus= topLeftTile
print(tileInFocus)
while nextS:
    if nextS != 'first':
        tileInFocus= nextS
    if input[tileInFocus]['s']:
        # def fixToMatch(tileNbr, side, matchSide):
        fixToMatch(input[tileInFocus]['s'],'n',input[tileInFocus]['img'][-1])
    nextS= input[tileInFocus]['s']
    newImgRow= []
    nextE= 'first'
    while nextE:
        if nextE != 'first':
            tileInFocus= nextE
        if input[tileInFocus]['e']:
            fixToMatch(input[tileInFocus]['e'],'w',getSides(tileInFocus)['right'])
        nextE= input[tileInFocus]['e']
        # print("tile: {}, next: {}".format(tileInFocus,nextE))
        newImgRow.append(tileInFocus)
        removeBorder(tileInFocus)
    bigImageTileNbrs.append(newImgRow)
bigImage= []
for tileNbrRows in bigImageTileNbrs:
    for i in range(len(input[tileNbrRows[0]]['img'])):
        imageRow= ""
        for tileNbr in tileNbrRows:
            imageRow+= input[tileNbr]['img'][i]
        bigImage.append(imageRow)

# for row in bigImage:
#     print(row)
input['bigImage']= {'img':bigImage,'c':0,'n':None,'e':None,'s':None,'w':None}
# for row in input['bigImage']['img']:
#     print(row)
# rotate('bigImage','r')
# print()
# flip('bigImage','v')
# for row in input['bigImage']['img']:
#     print(row)

input['binaryImage']= {'img':[],'c':0,'n':None,'e':None,'s':None,'w':None}
binImg= []
for row in input['bigImage']['img']:
    binImg.append(row.replace('.','0').replace('#','1'))
input['binaryImage']['img']= binImg

# prettyPrint({'bigImage':input['bigImage']})
# print()
# rotate('bigImage','r')
# prettyPrint({'bigImage':input['bigImage']})
# print()
# prettyPrint({'binaryImage':input['binaryImage']})

pattern=[
    int("00000000000000000010",2),
    int("10000110000110000111",2),
    int("01001001001001001000",2)
]
# print(pattern)
def findMonstersInBinary():
    foundMonsters= 0
    for i in range(len(input['binaryImage']['img'])-1):
        for j in range(len(input['binaryImage']['img'][i])):

            subStr0= input['binaryImage']['img'][i-1][j:j+20]
            subStr1= input['binaryImage']['img'][i][j:j+20]
            subStr2= input['binaryImage']['img'][i+1][j:j+20]
            if pattern[1] & int(subStr1,2) == pattern[1]:
                if pattern[2] & int(subStr2,2) == pattern[2]:
                    if pattern[0] & int(subStr0,2) == pattern[0]:
                        foundMonsters+= 1
    return foundMonsters

def findMonsters():
    nbrMonsters= findMonstersInBinary()
    if nbrMonsters:
        return nbrMonsters
    rotate('binaryImage','l')
    nbrMonsters= findMonstersInBinary()
    if nbrMonsters:
        return nbrMonsters
    rotate('binaryImage','l')
    nbrMonsters= findMonstersInBinary()
    if nbrMonsters:
        return nbrMonsters
    rotate('binaryImage','l')
    nbrMonsters= findMonstersInBinary()
    if nbrMonsters:
        return nbrMonsters
    flip('binaryImage','h')
    nbrMonsters= findMonstersInBinary()
    if nbrMonsters:
        return nbrMonsters
    rotate('binaryImage','l')
    nbrMonsters= findMonstersInBinary()
    if nbrMonsters:
        return nbrMonsters
    rotate('binaryImage','l')
    nbrMonsters= findMonstersInBinary()
    if nbrMonsters:
        return nbrMonsters
    rotate('binaryImage','l')
    nbrMonsters= findMonstersInBinary()
    if nbrMonsters:
        return nbrMonsters

nbrOnes= 0
for row in input['binaryImage']['img']:
    for x in row:
        nbrOnes+= int(x)

print(nbrOnes)
nbrFoundMonsters= findMonsters()
print(nbrFoundMonsters)
print(nbrOnes - nbrFoundMonsters*15)

    # print(input[row]['img'])
# prettyPrint({'2971':input['2971']})
# prettyPrint({'1171':input['1171']})

# prettyPrint({'1489':input['1489']})
# flip('1489','h')
# prettyPrint({'1489':input['1489']})
# flip('1489','v')
# prettyPrint({'1489':input['1489']})
# rotate('1489','l')
# prettyPrint({'1489':input['1489']})
# rotate('1489','r')
# prettyPrint({'1489':input['1489']})
# rotate(input[topLeftTile]['e'], 'e', getSides(topLeftTile)['right'])
# print(topLeftTile)
# updateTile('2473')
# prettyPrint(input)

endTime= time.time()
print("execution time: {}".format(endTime-startTime))

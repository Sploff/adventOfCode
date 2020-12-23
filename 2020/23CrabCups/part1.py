import copy, time
startTime= time.time()

def readFile(fileName):
    inputArray= []
    with open(fileName) as inputfile:
        for line in inputfile:
            inputArray.append(line.strip())
    return inputArray

cups= [1,5,7,6,2,3,9,8,4]
# Example
# cups= [3,8,9,1,2,5,4,6,7]

lastRound= 0
def printRound(round,cups,pick,cc,dc='X'):
    global lastRound
    if round != lastRound:
        lastRound= round
        print("---=== round {} ===---".format(round))
    # stringToPrint= ""
    # for cup in cups:
    #     if cup == cc:
    #         stringToPrint+= "({}) ".format(cup)
    #     elif cup == dc:
    #         stringToPrint+= "*{}* ".format(cup)
    #     elif cup in pick:
    #         stringToPrint+= "[{}] ".format(cup)
    #     else:
    #         stringToPrint+= "{} ".format(cup)
    # print(stringToPrint)
    print("{} {} {} {}".format(cc,cups,pick,dc))

def sortCups():
    while True:
        if cups[0] == 1:
            cups.pop(0)
            break
        cups.append(cups.pop(0))
    returnStr= ""
    for nbr in cups:
        returnStr+= str(nbr)
    return returnStr

round= 0
while round < 100:
    round+= 1
    currentCup= cups[0]
    pickedCups= []
    indexDC= None
    # printRound(round,cups,pickedCups,currentCup)
    cups.append(cups.pop(0))
    # printRound(round,cups,pickedCups,currentCup)
    pickedCups.append(cups.pop(0))
    pickedCups.append(cups.pop(0))
    pickedCups.append(cups.pop(0))
    # printRound(round,cups,pickedCups,currentCup)
    i= currentCup-1
    while True:
        if i < 0:
            i= 10
        if i in cups:
            indexDC= cups.index(i)
            break
        i-= 1
    for cup in pickedCups[::-1]:
        cups.insert(indexDC+1,cup)
    # printRound(round,cups,pickedCups,currentCup,cups[indexDC])
    # indexCC= cups.index(currentCup)
    # removedCups= cups[1:4]
    # printRound(round,cups,removedCups,cups[indexCC],7)

print(sortCups())

endTime= time.time()
print("execution time: {}".format(endTime-startTime))

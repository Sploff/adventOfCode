import copy, time
startTime= time.time()

cups= {1:5,5:7,7:6,6:2,2:3,3:9,9:8,8:4,4:10}
# Example
# cups= {3:8,8:9,9:1,1:2,2:5,5:4,4:6,6:7,7:10}
cc= 1
for i in range(10,1000001):
    # if i > 1000000:
    #     print(i)
    if i == 1000000:
        # print(i)
        cups[i]= cc
    else:
        cups[i]= i+1
cupsLen= len(cups)
pick= []
dc=None
# print(cupsLen)

def popPick():
    global cc
    pick.append(cups[cc])
    for _ in range(2):
        # print('pick',pick,pick[-1])
        # print('pick2',cups[pick[-1]])
        pick.append(cups[pick[-1]])
    cups[cc]= cups[pick[-1]]
    # print('cups',cups)
    # print('pop',pick)

def updateDC():
    global dc
    dc= cc - 1
    while True:
        if dc < 1:
            dc= cupsLen
        if dc in pick:
            dc-=1
        else:
            break
    # print('dc',dc)

def insertPick():
    global pick
    tmp= cups[dc]
    cups[dc]= pick[0]
    cups[pick[2]]= tmp
    pick= []
    # print('in',cups)

def printCups(startCup, nbrCups):
    nextCup= startCup
    toPrint= []
    i= 0
    while True and i < nbrCups:
        i+= 1
        toPrint.append(nextCup)
        nextCup= cups[nextCup]
        if nextCup == startCup:
            break
    print('List:',toPrint)

round= 0
while round < 10000000:
    round+= 1
    # printCups(cc)
    popPick()
    updateDC()
    insertPick()
    cc= cups[cc]
printCups(1, 20)

nbr1= cups[1]
nbr2= cups[nbr1]
print(nbr1*nbr2)

endTime= time.time()
print("execution time: {}".format(endTime-startTime))

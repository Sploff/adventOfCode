import copy, time
startTime= time.time()

def analyzeFile(fileName):
    global myTicket
    inputArray= []
    firstTicket= True
    with open(fileName) as inputfile:
        for line in inputfile:
            if "-" in line:
                type= line.strip().split(":")[0]
                types[type]= []
                ranges= line.strip()[line.index(":")+2:].split(" or ")
                for r in ranges:
                    r= r.split("-")
                    r[0]= int(r[0])
                    r[1]= int(r[1])
                    i= 0
                    while r[0] + i <= r[1]:
                        if r[0]+i not in types[type]:
                            types[type].append(r[0]+i)
                        if r[0]+i not in validNumbers:
                            validNumbers.append(r[0]+i)
                        i+= 1
            elif "," in line:
                ticket= []
                for x in line.strip().split(","):
                    ticket.append(int(x))
                if firstTicket:
                    myTicket= ticket
                    firstTicket= False
                if isValidTicket(ticket):
                    nearbyTickets.append(ticket)

    return inputArray

def isValidTicket(ticket):
    for x in ticket:
        if x not in validNumbers:
            return False
    return True

validNumbers= []
myTicket= None
nearbyTickets= []
types= {}

input= analyzeFile('input')
# input= analyzeFile('exampleInputPart2')

typeOrder= []
for i in range(len(types)):
    validTypeList= []
    for type in types:
        isValid= True
        for ticket in nearbyTickets:
            if ticket[i] not in types[type]:
                isValid= False
        if isValid:
            validTypeList.append(type)
    typeOrder.append(validTypeList)

continueFilter= True
notValidTypes= []
while continueFilter:
    continueFilter= False
    for type in typeOrder:
        if len(type) == 1:
            if type[0] not in notValidTypes:
                notValidTypes.append(type[0])
        else:
            continueFilter= True
            for t in type:
                if t in notValidTypes:
                    type.remove(t)

# print(validNumbers)
# print(nearbyTickets)
# print(types)
print(typeOrder)
# print(myTicket)

sumNumbers= 1
i= 0
for type in typeOrder:
    if "departure" in type[0]:
        sumNumbers*= myTicket[i]
    i+= 1

print(sumNumbers)

endTime= time.time()
print("execution time: {}".format(endTime-startTime))

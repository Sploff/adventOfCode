import copy, time
startTime= time.time()

def analyzeFile(fileName):
    global myTicket
    inputArray= []
    firstTicket= True
    with open(fileName) as inputfile:
        for line in inputfile:
            if "-" in line:
                ranges= line.strip()[line.index(":")+2:].split(" or ")
                for r in ranges:
                    r= r.split("-")
                    r[0]= int(r[0])
                    r[1]= int(r[1])
                    i= 0
                    while r[0] + i <= r[1]:
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
                else:
                    nearbyTickets.append(ticket)

    return inputArray

validNumbers= []
myTicket= None
nearbyTickets= []

input= analyzeFile('input')
# input= analyzeFile('exampleInput')

print(validNumbers)
print(myTicket)
print(nearbyTickets)

sumInvalidNumbrs= 0

for ticket in nearbyTickets:
    for x in ticket:
        if x not in validNumbers:
            sumInvalidNumbrs+= x

print(sumInvalidNumbrs)

endTime= time.time()
print("execution time: {}".format(endTime-startTime))

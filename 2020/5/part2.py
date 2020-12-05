def inputToArray(fileName):
    inputArray= []
    with open(fileName) as inputfile:
        for line in inputfile:
            inputArray.append(line.strip())
    return inputArray

input= inputToArray('input')
# input= inputToArray('exampleInput')

takenSeats= []
for x in range(1024):
    takenSeats.append(None)

def updateRow(seat,seatNumber):
    diff= int((seat["maxRow"] - seat["minRow"] + 1) / 2)
    if seatNumber[0] == "F":
        seat["maxRow"]-= diff
    else:
        seat["minRow"]+= diff
    if len(seatNumber) > 1:
        updateRow(seat,seatNumber[1:])

def updateCol(seat,seatNumber):
    diff= int((seat["maxCol"] - seat["minCol"] + 1) / 2)
    if seatNumber[0] == "L":
        seat["maxCol"]-= diff
    else:
        seat["minCol"]+= diff
    if len(seatNumber) > 1:
        updateCol(seat,seatNumber[1:])

for inputSeat in input:
    seat= {"number":inputSeat,"minRow":0,"maxRow":127,"minCol":0,"maxCol":7,"id":None}
    updateRow(seat,seat["number"][:7])
    updateCol(seat,seat["number"][7:])
    seat["id"]= seat["minRow"] * 8 + seat["minCol"]
    takenSeats[seat["id"]]= seat


for x in range(1024):
    if takenSeats[x] == None and takenSeats[x-1] and takenSeats[x+1]:
        print(x)

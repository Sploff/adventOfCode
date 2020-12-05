hex= '0123456789abcdefABCDEF'

def inputToArray(fileName):
    inputArray= []
    with open(fileName) as inputfile:
        for line in inputfile:
            inputArray.append(line.strip())
    return inputArray

def stringContainOnly(input, okList):
    return all(c in okList for c in input)

def stringContain(input, okList):
    return any(c in okList for c in input)

def stringContainOnlyDigits(input):
    return all(char.isdigit() for char in input)

input= inputToArray('input')
# input= inputToArray('exampleInput')

def updateRow(seat,seatNumber):
    # print(seat)
    # print(seatNumber)
    diff= int((seat["maxRow"] - seat["minRow"] + 1) / 2)
    if seatNumber[0] == "F":
        seat["maxRow"]-= diff
    else:
        seat["minRow"]+= diff
    if len(seatNumber) > 1:
        updateRow(seat,seatNumber[1:])

def updateCol(seat,seatNumber):
    # print(seat)
    # print(seatNumber)
    diff= int((seat["maxCol"] - seat["minCol"] + 1) / 2)
    if seatNumber[0] == "L":
        seat["maxCol"]-= diff
    else:
        seat["minCol"]+= diff
    if len(seatNumber) > 1:
        updateCol(seat,seatNumber[1:])

highestSeatId= 0
for inputSeat in input:
    seat= {"number":inputSeat,"minRow":0,"maxRow":127,"minCol":0,"maxCol":7,"id":None}
    updateRow(seat,seat["number"][:7])
    updateCol(seat,seat["number"][7:])
    seat["id"]= seat["minRow"] * 8 + seat["minCol"]
    if highestSeatId < seat["id"]:
        highestSeatId= seat["id"]
    print(seat)

print(highestSeatId)



# print(stringContain("hej",hex))
# print(stringContainOnly("fedeBeda",hex))
# print(stringContain("hoj",hex))
# print(stringContainOnly("fedeBedan",hex))
# print(stringContainOnlyDigits("13464"))
# print(stringContainOnlyDigits("134a64"))

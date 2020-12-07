hex= '0123456789abcdefABCDEF'

total= 0

def cleanInput(fileName):
    global total
    inputArray= []
    groupString= ""
    with open(fileName) as inputfile:
        for rawLine in inputfile:
            line= rawLine.strip()
            if line == "":
                inputArray.append(groupString)
                total+= len(groupString)
                groupString= ""
            else:
                for c in line:
                    if c not in groupString:
                        groupString+= c

        inputArray.append(groupString)
        total+= len(groupString)
    return inputArray

def stringContainOnly(input, okList):
    return all(c in okList for c in input)

def stringContain(input, okList):
    return any(c in okList for c in input)

def stringContainOnlyDigits(input):
    return all(char.isdigit() for char in input)

input= cleanInput('input')
input= cleanInput('exampleInput')

print("total: {}".format(total))

# print(stringContain("hej",hex))
# print(stringContainOnly("fedeBeda",hex))
# print(stringContain("hoj",hex))
# print(stringContainOnly("fedeBedan",hex))
# print(stringContainOnlyDigits("13464"))
# print(stringContainOnlyDigits("134a64"))

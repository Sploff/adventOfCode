neededContent= ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def inputToArray(fileName):
    inputArray= []
    with open(fileName) as inputfile:
        for line in inputfile:
            inputArray.append(line.strip().split(" "))
    return inputArray

input= inputToArray('input')
# input= inputToArray('exampleInput')

passports= []
validPp= 0
tmpPP= []

def addTmpToPp():
    global tmpPP, validPp
    tmpPpDict= {}
    for part in tmpPP:
        key, value = part.split(':')
        tmpPpDict[key]= value
    tmpPpDict['valid']= True
    for content in neededContent:
        if content not in tmpPpDict:
            tmpPpDict['valid']= False
    if tmpPpDict['valid']: validPp+=1
    passports.append(tmpPpDict)
    tmpPP=[]

for passPart in input:
    if passPart == ['']:
        addTmpToPp()
    else:
        tmpPP.extend(passPart)
addTmpToPp()

def printPassports():
    print("Passports:")
    for pp in passports:
        print(pp)

# printPassports()
print("Valid passports: {}".format(validPp))

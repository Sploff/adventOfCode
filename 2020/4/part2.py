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
    if tmpPpDict['valid']:
        hex= '0123456789abcdefABCDEF'
        eyeColor= ['amb','blu','brn','gry','grn','hzl','oth']
        if(
        int(tmpPpDict['byr'])<1920 or
        int(tmpPpDict['byr'])>2002 or
        int(tmpPpDict['iyr'])<2010 or
        int(tmpPpDict['iyr'])>2020 or
        int(tmpPpDict['eyr'])<2020 or
        int(tmpPpDict['eyr'])>2030
        ):
            tmpPpDict['valid']= False
        elif(
        (tmpPpDict['hgt'][-2:] != 'cm' and
        tmpPpDict['hgt'][-2:] != 'in')
        ):
            tmpPpDict['valid']= False
        elif(
        (tmpPpDict['hgt'][-2:] == 'cm' and
        (int(tmpPpDict['hgt'][:-2]) < 150 or
        int(tmpPpDict['hgt'][:-2]) > 193)) or
        (tmpPpDict['hgt'][-2:] == 'in' and
        (int(tmpPpDict['hgt'][:-2]) < 59 or
        int(tmpPpDict['hgt'][:-2]) > 76))
        ):
            # print(tmpPpDict['hgt'])
            tmpPpDict['valid']= False
        elif(
        tmpPpDict['hcl'][0] != '#' or
        len(tmpPpDict['hcl']) != 7 or not
        all(c in hex for c in tmpPpDict['hcl'][1:])
        ):
            # print(tmpPpDict['hcl'])
            tmpPpDict['valid']= False
        elif(
        tmpPpDict['ecl'] not in eyeColor
        ):
            # print(tmpPpDict['ecl'])
            tmpPpDict['valid']= False
        elif(
        len(tmpPpDict['pid']) != 9 or not
        all(char.isdigit() for char in tmpPpDict['pid'])
        ):
            print(tmpPpDict['pid'])
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

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

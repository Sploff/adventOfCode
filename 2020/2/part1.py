
inputList = []
with open('input') as inputfile:
    for line in inputfile:
        inputList.append(line.strip().replace(":", "").split(" "))

counter = 0

for pw in inputList:
    [charMin,charMax]= pw[0].split("-")
    if pw[2].count(pw[1]) >= int(charMin) and pw[2].count(pw[1]) <= int(charMax):
        counter+=1

print("number of OK passwords: {}".format(counter))

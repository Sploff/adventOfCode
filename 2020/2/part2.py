
inputList = []
with open('input') as inputfile:
    for line in inputfile:
        inputList.append(line.strip().replace(":", "").split(" "))

counter = 0

for [pos,char,pw] in inputList:
    pos= pos.split("-")
    if (pw[int(pos[0])-1] == char) ^ (pw[int(pos[1])-1] == char):
        counter+=1

print("number of OK passwords: {}".format(counter))

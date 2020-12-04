
inputList = []
with open('input') as inputfile:
    for line in inputfile:
        inputList.append(line.strip())

counter= 0
posX= 0
rowLength= len(inputList[0])

for row in inputList:
    if (row[posX%rowLength] == "#"): counter+=1
    posX+=3

print("number of trees: {}".format(counter))

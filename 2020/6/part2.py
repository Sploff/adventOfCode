total= 0

def countAnswers(fileName):
    global total
    groupSize= 0
    groupArray= []
    with open(fileName) as inputfile:
        for rawLine in inputfile:
            line= rawLine.strip()
            if line == "":
                groupSize= 0
                total+= len(groupArray)
                groupArray= []
            else:
                if groupSize == 0:
                    for c in line:
                        groupArray.append(c)
                else:
                    copyGroupArray= groupArray.copy()
                    for c in copyGroupArray:
                        if c not in line:
                            groupArray.remove(c)
                groupSize+= 1

        total+= len(groupArray)

input= countAnswers('input')
# input= countAnswers('exampleInput')

print("total: {}".format(total))

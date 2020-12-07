def analyzeInput(fileName):
    inputArray= []
    inputDict= {}
    with open(fileName) as inputfile:
        for line in inputfile:
            inputArray.append(line.strip().replace(" bags","").replace(" bag","").replace(".","").replace(" contain", ",").split(", "))
            key= None
            for x in inputArray[-1]:
                if not key:
                    key= x
                    inputDict[key]= []
                else:
                    nbrBags= x.split(" ")[0]
                    bagContent= x.replace(nbrBags+" ", "")
                    if bagContent != "other":
                        # inputDict[key].append({bagContent:nbrBags})
                        for x in range(int(nbrBags)):
                            inputDict[key].append(bagContent)
            key= None
    return inputDict

input= analyzeInput('input')
# input= analyzeInput('exampleInput')

def findColors(color, result):
    global input, counter
    for bagColor in input[color]:
        result.append(bagColor)
        findColors(bagColor, result)
    return result

listOfGold= findColors("shiny gold", [])
print(len(listOfGold))

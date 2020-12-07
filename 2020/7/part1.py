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
                    # inputDict[key].append({bagContent:nbrBags})
                    if bagContent != "other":
                        inputDict[key].append(bagContent)
            key= None
    return inputDict

input= analyzeInput('input')
# input= analyzeInput('exampleInput')

def findColors(color, result):
    global input
    for bagColor in input:
        if color in input[bagColor]:
            if bagColor not in result:
                result.append(bagColor)
                findColors(bagColor,result)
    return result

listOfGold= findColors("shiny gold", [])
print(len(listOfGold))

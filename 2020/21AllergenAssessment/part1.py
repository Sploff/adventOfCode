import copy, time
startTime= time.time()

def readFile(fileName):
    input= []
    with open(fileName) as inputfile:
        for line in inputfile:
            input.append(line.strip().replace(')','').split(" (contains "))
    return input

ingredients= {}

def addIngredients(row):
    for contain in row[1].split(', '):
        if contain not in ingredients:
            ingredients[contain]= row[0].split(' ')
        else:
            filteredList= []
            for cont in row[0].split(' '):
                if cont in ingredients[contain]:
                    filteredList.append(cont)
            ingredients[contain]= filteredList

def improveIngredientsList():
    for ingredientName in ingredients:
        if len(ingredients[ingredientName]) < 2:
            for ingredientName2 in ingredients:
                if ingredientName != ingredientName2:
                    if ingredients[ingredientName][0] in ingredients[ingredientName2]:
                        ingredients[ingredientName2].remove(ingredients[ingredientName][0])

dictionary= {}

def addToDictionary(row):
    for ingredient in row[0].split(' '):
        if ingredient not in dictionary:
            dictionary[ingredient]= None

def populateDictionary():
    for ingredient in ingredients:
        # print(ingredient)
        # print(ingredients[ingredient])
        dictionary[ingredients[ingredient][0]]= ingredient

def translateIngredients(inputList):
    for row in inputList:
        addToDictionary(row)
        addIngredients(row)
    improveIngredientsList()
    improveIngredientsList()
    improveIngredientsList()

def prettyPrint(toPrint):
    for row in toPrint:
        print("{}: {}".format(row,toPrint[row]))

def countSafeIngredients():
    rawIngredientsArray= []
    c= 0
    for row in input:
        for ingredient in row[0].split(' '):
            if not dictionary[ingredient]:
                c+= 1
    return c

input= readFile('input')
# input= readFile('exampleInput')
# prettyPrint(input)
# inputDict= listToDict(input)
# prettyPrint(inputDict)
translateIngredients(input)
prettyPrint(ingredients)
print()
# prettyPrint(dictionary)
populateDictionary()
print()
prettyPrint(dictionary)
print(countSafeIngredients())

endTime= time.time()
print("execution time: {}".format(endTime-startTime))

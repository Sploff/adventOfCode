import copy

results = []
with open('part1Input') as inputfile:
    for line in inputfile:
        results.append(int(line.strip()))

helpResults = copy.deepcopy(results)

product= 0

for x in results:
    helpResults.remove(x)
    for y in helpResults:
        sum = x + y
        if sum == 2020:
            print("x: {0}, y: {1}".format(x,y))
            product = x*y
            print(product)
            break
    if product != 0:
        break

print("Result: {0}".format(product))

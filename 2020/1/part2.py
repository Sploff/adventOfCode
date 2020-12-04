import copy

results = []
with open('part1Input') as inputfile:
    for line in inputfile:
        results.append(int(line.strip()))

helpResults1 = copy.deepcopy(results)
helpResults2 = copy.deepcopy(results)

product= 0

for x in results:
    helpResults1.remove(x)
    helpResults2.remove(x)
    for y in helpResults1:
        for z in helpResults2:
            sum = x + y + z
            if sum == 2020:
                print("x: {0}, y: {1}, z: {2}".format(x,y,z))
                product = x*y*z
                break
        if product != 0:
            break
    if product != 0:
        break

print("Result: {0}".format(product))

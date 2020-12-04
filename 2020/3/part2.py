trees= [0,0,0,0,0]
posX= [0,0,0,0,0]
deltaX= [1,3,5,7,0.5]
with open('input') as inputfile:
    for line in inputfile:
        for i in range(5):
            if (posX[i]%1==0 and line[int(posX[i]%len(line.strip()))] == "#"): trees[i]+=1
            posX[i]+=deltaX[i]
product= 1
for nbr in trees:
    product*= nbr
print("number of trees: product({})={}".format(trees, product))

import copy, time
startTime= time.time()

# input= readFile('input')
# input= {0:0,3:1,6:2}
# input= {1:0,3:1,2:2}
# input= {2:0,1:1,3:2}
# input= {3:0,1:1,2:2}
input= {1:0,0:1,16:2,5:3,17:4,4:5}

print(input)
# 0 3 3 1 0 4 0
# round= 2
# nextNumber= 6
round= 5
nextNumber= 4
while round < 30000000-1:
    # if round > 30000000 - 10:
    #     print(str(round) +": "+ str(nextNumber))
    if nextNumber not in input:
        input[nextNumber]= round
    diff= round - input[nextNumber]
    input[nextNumber]= round
    nextNumber= diff
    round+= 1

print(nextNumber)

endTime= time.time()
print("execution time: {}".format(endTime-startTime))

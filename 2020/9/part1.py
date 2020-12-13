def analyzeInput(fileName):
    inputArray= []
    with open(fileName) as inputfile:
        for line in inputfile:
            inputArray.append(int(line.strip()))
    return inputArray

input= analyzeInput('input')
# input= analyzeInput('exampleInput')

preamble= 25
invalidRow= 0

def rowValidator(rowNbr):
    global invalidRow
    compArray= input[rowNbr-preamble:rowNbr]
    valid= False
    for x in compArray:
        for y in compArray:
            # print("comp: {}, x: {}, y: {}, sum: {}".format(input[rowNbr], x, y, x+y))
            if x != y and x+y == input[rowNbr]:
                valid= True
    if valid:
        rowNbr+= 1
        rowValidator(rowNbr)
    else:
        invalidRow= rowNbr

rowValidator(preamble)
print("row: {} ({})".format(invalidRow,input[invalidRow]))

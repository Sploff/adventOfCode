def analyzeInput(fileName):
    inputArray= []
    with open(fileName) as inputfile:
        for line in inputfile:
            inputArray.append(int(line.strip()))
    return inputArray

input= analyzeInput('exampleInput')
input= analyzeInput('input')

preamble= 25
invalidRow= 0
invalidNbr= 0
# magicNumber= 14360655


def getMagicNumber(rowNbr):
    global invalidRow, invalidNbr
    compArray= input[rowNbr-preamble:rowNbr]
    valid= False
    for x in compArray:
        for y in compArray:
            # print("comp: {}, x: {}, y: {}, sum: {}".format(input[rowNbr], x, y, x+y))
            if x != y and x+y == input[rowNbr]:
                valid= True
    if valid:
        rowNbr+= 1
        getMagicNumber(rowNbr)
    else:
        invalidRow= rowNbr
        invalidNbr= input[rowNbr]

getMagicNumber(preamble)
print("row: {} ({})".format(invalidRow,invalidNbr))

def validateNumbers(rowNbr):
    global invalidRow, invalidNbr
    startRow= rowNbr-preamble
    endRow= rowNbr
    compArray= input[startRow:endRow]

    valid= False
    for testLength in range(preamble):
        for pos in range(preamble):
            if pos + testLength +1 < len(compArray):
                sum= 0
                nbrs= []
                startPos= pos
                endPos= pos+testLength+1
                # print("row: {}, start: {}, end: {}".format(rowNbr,startPos,endPos))
                for x in compArray[startPos:endPos]:
                    sum+= x
                    nbrs.append(x)
                if sum == invalidNbr:
                    print(invalidNbr)
                    print(nbrs)
                    print("{}+{}= {}".format(min(nbrs),max(nbrs),min(nbrs)+max(nbrs)))
                    return
    rowNbr+= 1
    validateNumbers(rowNbr)



validateNumbers(preamble)
# print("row: {} ({})".format(invalidRow,input[invalidRow]))

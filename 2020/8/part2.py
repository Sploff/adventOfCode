def analyzeInput(fileName):
    inputArray= []
    with open(fileName) as inputfile:
        for line in inputfile:
            inputArray.append(line.strip().split(" "))
    return inputArray

program= analyzeInput('input')
# program= analyzeInput('exampleInput')

accumulator= 0
rowNbr= 0

def runProgram(tmpProgram, visitedRows):
    global accumulator, rowNbr
    if rowNbr not in visitedRows:
        visitedRows.append(rowNbr)
        # print(tmpProgram[rowNbr])
        if tmpProgram[rowNbr][0] == 'acc':
            accumulator+= int(tmpProgram[rowNbr][1])
            rowNbr+= 1
        elif tmpProgram[rowNbr][0] == 'nop':
            rowNbr+= 1
        elif tmpProgram[rowNbr][0] == 'jmp':
            rowNbr+= int(tmpProgram[rowNbr][1])
        # print(rowNbr)
        if rowNbr > 0 and rowNbr < len(tmpProgram):
            runProgram(tmpProgram, visitedRows)
            return rowNbr
    return None

lineNbr= 0
for instr in program:
    if instr[0] != 'acc':
        accumulator= 0
        rowNbr= 0
        tmpProgram= program.copy()
        if instr[0] == 'nop':
            tmpProgram[lineNbr]= ['jmp',instr[1]]
        elif instr[0] == 'jmp':
            tmpProgram[lineNbr]= ['nop',instr[1]]
        # print(tmpProgram)
        exitRowNbr= runProgram(tmpProgram,[])
        if exitRowNbr and exitRowNbr == len(tmpProgram):
            print("prog length: {}".format(len(tmpProgram)))
            print("rowNbr: {}".format(rowNbr))
            print(accumulator)
    lineNbr+=1

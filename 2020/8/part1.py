def analyzeInput(fileName):
    inputArray= []
    inputDict= {}
    with open(fileName) as inputfile:
        for line in inputfile:
            inputArray.append(line.strip().split(" "))
    return inputArray

program= analyzeInput('input')
# program= analyzeInput('exampleInput')

accumulator= 0
visitedRows= []

def runProgram(rowNbr):
    global program, visitedRows, accumulator
    if rowNbr not in visitedRows:
        visitedRows.append(rowNbr)
        print(program[rowNbr])
        if program[rowNbr][0] == 'acc':
            accumulator+= int(program[rowNbr][1])
            rowNbr+= 1
        elif program[rowNbr][0] == 'nop':
            rowNbr+= 1
        elif program[rowNbr][0] == 'jmp':
            rowNbr+= int(program[rowNbr][1])
        print(rowNbr)
        runProgram(rowNbr)


runProgram(0)
print(accumulator)

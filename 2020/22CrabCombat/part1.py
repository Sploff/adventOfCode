import copy, time
startTime= time.time()

def readFile(fileName):
    decks= {}
    player= None
    with open(fileName) as inputfile:
        for line in inputfile:
            row= line.strip()
            if len(row) < 1:
                None
            elif ':' in row:
                player= row.replace(':','')
                decks[player]= []
            else:
                decks[player].append(int(row))
    return decks

def playRound():
    p1= decks['Player 1'].pop(0)
    p2= decks['Player 2'].pop(0)
    if p1 > p2:
        decks['Player 1']+= [p1,p2]
    else:
        decks['Player 2']+= [p2,p1]

def playGame():
    continuePlay= True
    while continuePlay:
        playRound()
        if len(decks['Player 1'])<1:
            return 'Player 2'
        elif len(decks['Player 2'])<1:
            return 'Player 1'

def calcScore(deck):
    score= 0
    i= 0
    for card in deck[::-1]:
        i+= 1
        score+= card * i
    return score

decks= readFile('input')
# decks= readFile('exampleInput')
winner= playGame()
score= calcScore(decks[winner])
print(winner)
print(decks)
print(score)

endTime= time.time()
print("execution time: {}".format(endTime-startTime))

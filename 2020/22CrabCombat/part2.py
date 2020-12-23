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

game= 0
def playRound(deck1,deck2):
    p1= deck1.pop(0)
    p2= deck2.pop(0)
    if p1 <= len(deck1) and p2 <= len(deck2):
        # print("   game: {}\n   deck1: {} deck2: {}".format(game,deck1,deck2))
        winner= playGame(deck1.copy()[:p1],deck2.copy()[:p2])
        # print("   game: {}\n   deck1: {} deck2: {}".format(game,deck1,deck2))
        if winner == 'Player 1':
            deck1+= [p1,p2]
        else:
            deck2+= [p2,p1]
    elif p1 > p2:
        deck1+= [p1,p2]
    else:
        deck2+= [p2,p1]

def playGame(deck1,deck2):
    global game
    game+= 1
    thisGame= game
    # print("game: {}\ndeck1: {}\ndeck2: {}".format(game,deck1,deck2))
    history= []
    continuePlay= True
    while continuePlay:
        comb= deck1 + ['-'] + deck2
        if comb in history:
            print('Loop found. Aborting game')
            print("LOOP: {}, deck1: {}, deck2: {}".format(thisGame,deck1,deck2))
            return 'Player 1'
        else:
            history.append(comb)
        print("game: {}, deck1: {}, deck2: {}".format(thisGame,deck1,deck2))
        playRound(deck1,deck2)
        if len(deck1)<1:
            return 'Player 2'
        elif len(deck2)<1:
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
winner= playGame(decks['Player 1'],decks['Player 2'])
score= calcScore(decks[winner])
print(winner)
print(decks)
print(score)

endTime= time.time()
print("execution time: {}".format(endTime-startTime))

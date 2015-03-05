import random

intToMoveDict = {0:'rock', 1:'paper', 2:'scissors'}

rochambeauWins = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}

def computerGene():
    computerMoveInt = random.randint(0,2)
    computerMove = intToMoveDict[computerMoveInt]
    return computerMove


def judgeWins(playerMove):
    computerMove = computerGene()
    print("Computer Move is {}".format(computerMove))
    if rochambeauWins[playerMove] == computerMove:
        return("Player wins")
    elif rochambeauWins[computerMove] == playerMove:
        return("Computer wins")
    else:
        return("Draw")


if __name__ == '__main__':
    while True:
        playerChoice = input("Input a choice(rock/paper/scissors)")
        if playerChoice == '' or playerChoice == 'q' or playerChoice == 'Q':
            break;
        print(judgeWins(playerChoice))

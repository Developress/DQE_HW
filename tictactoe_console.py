import random

def showGameboard():
    print("-------------")
    for i in range(3):
        print("|", gameboard[0 + i * 3], "|", gameboard[1 + i * 3], "|", gameboard[2 + i * 3], "|")
    print("-------------")

def makeMove():
    global mode
    global move
    global player
    global computerMove
    if mode == 1 and computerMove:
        print("Computer moves: ")
        move = random.randint(1, 9)
        while gameboard[move - 1] == "X" or gameboard[move - 1] == "O":
            move = random.randint(1, 9)
        computerMove = False
    else:
        print(player, "moves: ")
        move = int(input())
        if mode == 1:
            computerMove = True
    if move in range(1,10) and gameboard[move-1] != "X" and gameboard[move-1] != "O":
        gameboard[move-1] = player
    else:
        print("Invalid move! Try again")
        makeMove()
        if mode == 1:
            computerMove = False

def checkForWin():
    for i in winCombinations:
        for j in i:
           if gameboard[j-1] != player:
               win = False
               break
           else:
               win = True
        if win:
            return True
    return False


gameboard = list(range(1, 10))
move = -1
player = "X"
extra = "O"
mode = int(input("Choose a mode to play:\n"
             "[1] - with computer\n"
             "[2] - two players\n"))

while not (mode in range(1,3)):
    print("Invalid input. Try again!")
    mode = int(input("Choose a mode to play:\n"
                 "[1] - with computer\n"
                 "[2] - two players\n"))

if mode == 1:
    choise = int(input("Choose a player:\n"
                 "X - [1]\n"
                 "O - [2]\n"))

    while choise!=1 and choise!=2:
        print("Invalid input! Try again")
        player = int(input("Choose a player:\n"
                 "X - [1]\n"
                 "O - [2]\n"))

    if choise == 1:
        computerMove = False
    else:
        computerMove = True

showGameboard()
winCombinations = ((1,2,3),(4,5,6),(7,8,9), (1,4,7),(2,5,8),(3,6,9),(1,5,9),
                   (3,5,7))
i = 0

while True:
    makeMove()
    showGameboard()

    if checkForWin():
        if mode == 1 and not computerMove:
            print("Computer won!")
        else:
            print(player, "won!")
        break

    i+=1
    if i == 9:
        print("Draw")
        break
    player, extra = extra, player

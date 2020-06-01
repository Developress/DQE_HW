import random


def show_game_board():
    """Print the game_board on the screen"""
    print("-------------")
    for i in range(3):
        print("|", game_board[0 + i * 3], "|", game_board[1 + i * 3], "|", game_board[2 + i * 3], "|")
    print("-------------")


def make_move():
    """
        Let the computer or the user make the move
        :raises ValueError: when the input is incorrect
    """
    global mode
    global move
    global player
    global computer_move

    # if the user plays with the computer and computer needs to move
    if mode == 1 and computer_move:
        print("Computer moves: ")
        # generates the random move
        move = random.randint(1, 9)

        # if the field is occupied, generates the random move again
        while game_board[move - 1] == "X" or game_board[move - 1] == "O":
            move = random.randint(1, 9)

        computer_move = False

    # the user makes the move
    else:
        print(player, "moves: ")

        # loop until the input is correct
        while True:
            try:
                move = int(input())
                break
            except ValueError:
                print("Invalid input! Please, make another move")

        # if the user plays with the computer, then let the computer move next
        if mode == 1:
            computer_move = True

    # if the input is correct and field is not occupied, then occupy it
    if move in range(1, 10) and game_board[move - 1] != "X" and game_board[move - 1] != "O":
        game_board[move - 1] = player

    # if the field is already occupied
    else:
        print("The field is occupied! Please, make another move")

        # if the user plays with the computer, then cancel the computer move
        # to let the user move again
        if mode == 1:
            computer_move = False

        # make one more move
        make_move()


def check_for_win():
    """
        Check all the win combinations to confirm the victory
        :return: True if the victory is confirmed, False if not
    """

    for i in win_combinations:
        win = False

        for j in i:
            # if the field from the win combination matches with the player
            # then assign win to True
            if game_board[j - 1] == player:
                win = True

            # if the field from the win combination does not match with the player
            # then stop checking the current combination and check the next one
            else:
                win = False
                break

        # if the loop has not been breaking, then the victory is confirmed
        if win:
            return True

    # if the loop has been breaking all the time, then the victory is not confirmed
    return False


# initialize everything before the start of the game
game_board = list(range(1, 10))
move = 0
counter = 0
player = "X"
extra = "O"
computer_move = False
win_combinations = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9),
                    (1, 5, 9), (3, 5, 7))

print("Welcome to the tic tac toe game!")

# loop until the input is correct
while True:
    try:
        mode = int(input("Choose a mode to play:\n"
                         "[1] - with computer\n"
                         "[2] - two players\n"))
        while not (mode in range(1, 3)):
            print("Invalid input. Try again!")
            mode = int(input("Choose a mode to play:\n"
                             "[1] - with computer\n"
                             "[2] - two players\n"))
        break
    except ValueError:
        print("Invalid input! Try again")

# if the user plays with the computer, then ask him whether he requires the first move
if mode == 1:
    choice = input("Do you require the first move? Enter y if yes, another key if no\n")

    # if the input is different from "y", then the user does not require the first move
    # so the computer moves first
    if choice != "y":
        computer_move = True

print("\nTo make the move, please enter the appropriate number, "
      "which corresponds to the position of the field")
show_game_board()

while True:
    make_move()
    show_game_board()

    if check_for_win():
        # if the user plays with the computer and computer has moved recently
        if mode == 1 and not computer_move:
            print("Computer won!")
        # if the user has moved recently
        else:
            print(player, "won!")
        break

    counter += 1

    # if all the fields are occupied, then confirm the draw
    if counter == 9:
        print("Draw")
        break

    # change the active player
    player, extra = extra, player

from board import *


needInstructions = input("Welcome to Battleship!\nDo you know how to play? (y/n) ")
if needInstructions == "n":
    print("Instructions")

playerCount = None
while playerCount == None:
    playerCount = input("How many players? ")
    try:
        playerCount = int(playerCount)
        if playerCount > 2 or playerCount < 1:
            raise Exception(None)
    except:
        print("Invalid choice, please enter a valid number (1 or 2)")
        playerCount = None

# Set up the players
board = Board(playerCount)
game = True
turnCount = 0

# Play the game!
while game:
    turnCount += 1
    board.print_board()
    board.user_take_turn()
    if playerCount == 2:
        board.computer_take_turn()
    winningMessage = board.has_someone_won_yet()
    if winningMessage:
        game = False
        board.print_board()
        print(winningMessage)
        print("The game is over after", turnCount, "turns")

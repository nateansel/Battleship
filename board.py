from player import *




class Board:
    def __init__(self, playerCount):
        self.player1 = None
        self.player2 = None

        self.player1 = Player(isComputer=True)
        if playerCount == 2:    # We must be playing against the computer and the computer against us
            self.player2 = Player()
        return




    def user_take_turn(self):
        idiot = True
        # Just ask the user for a coordinate repeatedly until they do it right. (idiots)
        while idiot:
            tempCoordinates = input("Choose a coordinate to shoot (x,y): ")
            tempCoordinates = analyze_coordinates(tempCoordinates)
            while tempCoordinates == None:
                tempCoordinates = input("Choose a coordinate to shoot (x,y): ")
                tempCoordinates = analyze_coordinates(tempCoordinates)
            if self.player1.has_shot_before(tempCoordinates[0], tempCoordinates[1]):
                print("You already shot there, try again.")
            else:
                self.player1.register_shot(tempCoordinates[0], tempCoordinates[1])
                idiot = False
        return





    def computer_take_turn(self):
        # The computer is not an idiot
        shot = self.player1.turn_from_computer()
        didShotHit = self.player2.register_shot(shot[0], shot[1])
        if didShotHit:
            # If the ship wasn't sunk try to hit it some more
            self.player1.generate_could_be_ships(shot[0], shot[1])
        return






    def print_board(self):
        # Don't try to follow this method, it's terrible
        global HEIGHT
        global WIDTH
        # This didn't work in IDLE :(
        subprocess.call("clear")
        toPrint = ""
        beginning = True
        for i in range(HEIGHT):
            for j in range(WIDTH):
                if beginning:
                    toPrint += "   " + ("  " * (WIDTH // 2)) + " X\n   "
                    for each in range(WIDTH):
                        toPrint += " " + str(each)
                    toPrint += "\n   " + (" _" * WIDTH) + "\n"
                    beginning = False
                # If not the middle of the board
                if j == 0 and i != HEIGHT // 2:
                    toPrint += "  " + str(i)
                # If middle of the board
                elif j == 0 and i == HEIGHT // 2:
                    toPrint += "Y " + str(i)
                # A shot has hit this part of the board
                if [j, i] in self.player1.shotsTaken:
                    if self.player1.ship1.is_hit_by_shot(j, i) or self.player1.ship2.is_hit_by_shot(j, i):
                        toPrint += "|X"
                    else:
                        toPrint += "|•"
                # A shot hasn't hit here
                else:
                    toPrint += "|_"
                if j == WIDTH - 1:
                    toPrint += "|\n"
        if player2:
            # Seperate the boards
            toPrint += "\n"
            beginning = True
            for i in range(HEIGHT):
                for j in range(WIDTH):
                    if beginning:
                        toPrint += "   " + ("  " * (WIDTH // 2)) + " X\n   "
                        for each in range(WIDTH):
                            toPrint += " " + str(each)
                        toPrint += "\n   " + (" _" * WIDTH) + "\n"
                        beginning = False
                    if j == 0 and i != HEIGHT // 2:
                        toPrint += "  " + str(i)
                    elif j == 0 and i == HEIGHT // 2:
                        toPrint += "Y " + str(i)
                    if self.player2.ship1.is_hit_by_shot(j, i) or self.player2.ship2.is_hit_by_shot(j, i):
                        # One of my ships is here and it has been hit
                        if [j, i] in self.player2.shotsTaken:
                            toPrint += "|X"
                        # One of my ships is here
                        else:
                            toPrint += "|+"
                    elif [j, i] in self.player2.shotsTaken:
                        toPrint += "|•"
                    else:
                        toPrint += "|_"
                    if j == WIDTH - 1:
                        toPrint += "|\n"
        print(toPrint)
        return





    def has_someone_won_yet(self):
        # Return the winning message
        if self.player1.ship1.sunk and self.player1.ship2.sunk:
            return "You won! Congradulations! You should play more often, you're pretty good!"
        elif self.player2 and self.player2.ship1.sunk and self.player2.ship2.sunk:
            return "The computer won this game. Play again sometime!"
        return None




if __name__ == "__main__":
    b = Board(1)
    for i in range(HEIGHT):
        for j in range(WIDTH):
            b.player1.register_shot(i, j)
    b.print_board()

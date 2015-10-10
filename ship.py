from battleship_helper import *



class Ship:
    def __init__(self, isComputer=False, otherShip=None):
        self.coordinates = [[-1,-1], [-1,-1]]
        self.sunk = False
        self.hitCoordinate = -1
        # If this is the computer's ship, set it up
        if isComputer:
            self.computer_place_ship(otherShip)
        return



    def computer_place_ship(self, otherShip=None):
        global HEIGHT
        global WIDTH
        placed = False

        # While the ship has not been placed because of error somewhere, illegal placement, etc.
        while not placed:
            # Assume the ship will be placed
            placed = True
            while self.coordinates[0][0] == -1:
                # Randomly come up with a first coordinate
                self.coordinates[0][0] = random.randint(0, WIDTH - 1)
                self.coordinates[0][1] = random.randint(0, HEIGHT - 1)
                # Make sure this coordinate isn't on some other ship
                if otherShip and otherShip.is_hit_by_shot(self.coordinates[0][0], self.coordinates[0][1]):
                    self.coordinates[0][0] = -1

            # Build a list of coordinates around the first one to choose from randomly
            x = self.coordinates [0][0]
            y = self.coordinates [0][1]
            tempCoordinatesList = [[x + 1, y], [x, y + 1], [x - 1, y], [x, y - 1]]
            random.shuffle(tempCoordinatesList)

            # Get the second coordinate
            self.coordinates[1] = tempCoordinatesList.pop()
            # Continue checking the coordinates until one is found to be legal (on the board and not a part of the other ship)
            while True:
                if is_coordinate_on_board(self.coordinates[1][0], self.coordinates[1][1]):
                    if otherShip and otherShip.is_hit_by_shot(self.coordinates[1][0], self.coordinates[1][1]):
                        if len(tempCoordinatesList) != 0:
                            self.coordinates[1] = tempCoordinatesList.pop()
                        else:
                            # No more coordinates to try so this placement is illegal
                            placed = False
                            break
                    else:
                        break
                else:
                    if len(tempCoordinatesList) != 0:
                        self.coordinates[1] = tempCoordinatesList.pop()
                    else:
                        # No more coordinates to try so this placement is illegal
                        placed = False
                        break
        return






    def user_place_ship(self, shipNum, otherShip=None):
        global HEIGHT
        global WIDTH
        tempCoordinate = None

        # Ask the user for the first set of coordinates
        while tempCoordinate == None:
            print("Pick a coordinate for the ", shipNum, " ship (x,y): ", end="")
            tempCoordinate = input()
            tempCoordinate = analyze_coordinates(tempCoordinate)
            if otherShip and tempCoordinate and otherShip.is_hit_by_shot(tempCoordinate[0], tempCoordinate[1]):
                print("That coordinate is a part of your other ship, try again.")
                tempCoordinate = None
        self.coordinates[0] = tempCoordinate

        # Ask the user for the second coordinate (they can choose from a list of 2-4 coordinates)
        print("Choose a second coordinate (type the number associated with the coordinate):")
        count = 0
        tempCoordinateList = []
        x = 0
        y = 0

        # Ask the user for any of the following coordinates (only if they are legal)
        # TOP
        x = self.coordinates[0][0]
        y = self.coordinates[0][1] + 1
        printThis = False
        if is_coordinate_on_board(x, y):
            if otherShip:
                if not otherShip.is_hit_by_shot(x, y):
                    printThis = True
            else:
                printThis = True
        if printThis:
            print((count + 1), ". (", x, ",", y, ") above", sep="")
            tempCoordinateList.append([x, y])
            count += 1

        # BOTTOM
        x = self.coordinates[0][0]
        y = self.coordinates[0][1] - 1
        printThis = False
        if is_coordinate_on_board(x, y):
            if otherShip:
                if not otherShip.is_hit_by_shot(x, y):
                    printThis = True
            else:
                printThis = True
        if printThis:
            print((count + 1), ". (", x, ",", y, ") below", sep="")
            tempCoordinateList.append([x, y])
            count += 1

        # RIGHT
        x = self.coordinates[0][0] + 1
        y = self.coordinates[0][1]
        printThis = False
        if is_coordinate_on_board(x, y):
            if otherShip:
                if not otherShip.is_hit_by_shot(x, y):
                    printThis = True
            else:
                printThis = True
        if printThis:
            print((count + 1), ". (", x, ",", y, ") right", sep="")
            tempCoordinateList.append([x, y])
            count += 1

        # LEFT
        x = self.coordinates[0][0] - 1
        y = self.coordinates[0][1]
        printThis = False
        if is_coordinate_on_board(x, y):
            if otherShip:
                if not otherShip.is_hit_by_shot(x, y):
                    printThis = True
            else:
                printThis = True
        if printThis:
            print((count + 1), ". (", x, ",", y, ") left", sep="")
            tempCoordinateList.append([x, y])
            count += 1

        # Make sure the input is valid
        while True:
            secondCoordinateChoice = input("Second coordinate choice: ")
            # Try converting it to an int value
            try:
                secondCoordinateChoice = int(secondCoordinateChoice)
            except:
                print("Not a valid choice, try again.")
                continue
            # See if it is in a valid range
            if secondCoordinateChoice > -1 and secondCoordinateChoice < count + 1:
                self.coordinates[1] = tempCoordinateList[secondCoordinateChoice - 1]
                break
            else:
                print("Not a valid choice, try again.")

        # Finally exit the method
        return




    def is_hit_by_shot(self, x, y):
        if (x == self.coordinates[0][0] and y == self.coordinates[0][1]) or (x == self.coordinates[1][0] and y == self.coordinates[1][1]):
            return True
        return False        # Executes only if the above if condition fails (saves you an else line)





    def register_hit(self, x, y):
        if self.is_hit_by_shot(x, y):     # A check to see if the ship was hit with this shot
            if self.hitCoordinate == -1:  # This is -1 if the ship hasn't been hit yet, meaning this shot won't sink it
                if self.coordinates[0][0] == x and self.coordinates[0][1] == y:
                    self.hitCoordinate = 0
                else:
                    self.hitCoordinate = 1
            else:
                self.sunk = True
        else:
            print("ERROR: The ship was not actually hit.")
        return





if __name__ == "__main__":
    s = Ship()
    s.user_place_ship(1)

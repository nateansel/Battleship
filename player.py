from ship import *


class Player:
    def __init__(self, isComputer=False):
        self.ship1 = Ship(isComputer)
        self.ship2 = Ship(isComputer, otherShip=self.ship1)
        self.shotsTaken = []
        self.numberOfShotsTaken = 0
        self.isComputer = isComputer

        # Computer variables
        self.shotsToTake = []
        self.couldBeShips = []

        if not isComputer:
            self.ship1.user_place_ship("first")
            self.ship2.user_place_ship("second", otherShip=self.ship1)
        else:
            # Gonna build up a list of shots for the computer to take during the game
            global HEIGHT
            global WIDTH
            odd = 1
            # For every number between 0 and WIDTH (default is 5)
            for i in range(WIDTH):
                for j in range(odd, HEIGHT, 2):
                    self.shotsToTake.append([i, j])
                if odd:
                    odd = 0
                else:
                    odd = 1
            # Shuffle the list so popping is shuffled
            random.shuffle(self.shotsToTake)
        return




    def register_shot(self, x, y):
        # A check for if the shot has been registered yet or not, if so there was an error
        if not self.has_shot_before(x, y):
            self.shotsTaken.append([x, y])
            # Register the shot with either ship
            if self.ship1.is_hit_by_shot(x, y):
                self.ship1.register_hit(x, y)
                if self.ship1.sunk == False:
                    if not self.isComputer:
                        print("The computer hit one of your ships!")
                        # Return True so that the computer will generate a list of shots to take around this one
                        return True
                    else:
                        print("You hit a ship!")
                        return True
                else:
                    if not self.isComputer:
                        print("The computer sunk one of your ships!")
                        return False
                    else:
                        print("You sunk a ship!")
                        return False
            elif self.ship2.is_hit_by_shot(x, y):
                self.ship2.register_hit(x, y)
                if self.ship2.sunk == False:
                    if not self.isComputer:
                        print("The computer hit one of your ships!")
                        return True
                    else:
                        print("You hit a ship!")
                        return True
                else:
                    if not self.isComputer:
                        print("The computer sunk one of your ships!")
                        return False
                    else:
                        print("You sunk a ship!")
                        return False
        else:
            print("That space has already been shot.")
        return




    def has_shot_before(self, x, y):
        if [x, y] in self.shotsTaken:
            return True
        return False




    def turn_from_computer(self):
        # If there are shots that should be prioritized take one of them, otherwise take a normal shot
        if len(self.couldBeShips) > 0:
            toReturn = self.couldBeShips.pop()
        else:
            toReturn = self.shotsToTake.pop()
        return toReturn




    def generate_could_be_ships(self, x, y):
        # TOP
        if is_coordinate_on_board(x, y + 1):
            self.couldBeShips.append([x, y + 1])
        # BOTTOM
        if is_coordinate_on_board(x, y - 1):
            self.couldBeShips.append([x, y - 1])
        # RIGHT
        if is_coordinate_on_board(x + 1, y):
            self.couldBeShips.append([x + 1, y])
        # LEFT
        if is_coordinate_on_board(x - 1, y):
            self.couldBeShips.append([x - 1, y])
        random.shuffle(self.couldBeShips)
        return





if __name__ == "__main__":
    p = Player(True)
    print(p.ship1.coordinates, "\n", p.ship2.coordinates)
    print(p.has_shot_before(0, 0))
    p.register_shot(0, 0)
    print(p.has_shot_before(0, 0))

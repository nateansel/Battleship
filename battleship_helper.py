# Imports
import random
import subprocess



# Board dimensions
HEIGHT = 5
WIDTH = 5




def analyze_coordinates(coordinates):
    global HEIGHT
    global WIDTH

    coordinates = coordinates.split(",")

    # Try to convert the coordinates to int values
    for i in range(len(coordinates)):
        try:
            coordinates[i] = int(coordinates[i])
        except:
            print("You entered the coordinates in the wrong format, please follow this example: \"x,y\"")
            return None

    # Are there too many coordinates?
    if len(coordinates) == 2:
        if is_coordinate_on_board(coordinates[0], coordinates[1]):
            return coordinates
        else:
            print("The coordinates you entered were not in range, acceptable ranges are x: 0-", (WIDTH - 1), " and y: 0-", (HEIGHT - 1), sep="")
    else:
        print("You entered the coordinates in the wrong format, please follow this example: \"x,y\"")

    # Return None, which is a cue to the program that an error occured
    return None




def is_coordinate_on_board(x, y):
    return x < WIDTH and x > -1 and y < HEIGHT and y > -1



if __name__ == "__main__":
    print(analyze_coordinates("1,6"))

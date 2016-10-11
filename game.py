from map import rooms
from player import *
from items import *
from gameparser import *


def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:

    """
    return chosen_exit in exits

def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:

    """

    # Next room to go to
    return rooms[exits[direction]]

def win_lose():
    """Check if the player has met the conditions of a win or a loss and sets the approprate variable.
    A return statement is not required.

    """

# Declare as global for use
global victory
global loss

#Init
def main():

    # Game loop
    while True:
        # Display status
        # Show possible actions
        # Execute input
        # Exit(Win/Lose)

# Initialise main
if __name__ == "__main__":
    main()
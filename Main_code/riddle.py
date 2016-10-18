from map import rooms
from items import *
from gameparser import *
from random import randint

"""

##########
Riddle One
##########

first part of the puzzles for the 'Old Green Tree'.


Also to be added:
					-Locked Office
					-Office Window
					-Jacket/Safe
					-Safe code puzzle
					-Clue for next puzzle



"""




def riddle_OGT():
	# if room['name'] == 'room_The_Old_Green_Tree':
    print("\nI don't have eyes, but once I did see. Once I had thoughts, but now I'm white and empty.")
    print("What am I?\n")
    answer = input("> ")
    normalise_input(answer)
    if answer == 'skull':
        print("Correct\n")
    else:
        print('\nThink more halloween!\n')
        riddle_OGT()



"""


##########
Riddle Two
##########

Puzzle for 'The Fat Angel' pub.

Also to be added:
					-Second structure to puzzle
					-Possible third
					-clue to third puzzle





"""


def riddle_TFA():
	# if room['name'] == 'room_The_Fat_Angel':
    print("#################################################")
    print("I am the first on Earth,")
    print("The second in Heaven,")
    print("I appear two times in a week,")
    print("you can only see me once in a year, although I am in the middle to the sea.")
    print("What am i?\n")
    answer = input("> ")
    normalise_input(answer)
    if answer == 'e'or answer == 'E':
        print("\nCorrect\n")
    else:
        print("\nRead the sentence closely\n")
        riddle_TFA()


"""

############
Riddle Three
###########

"""
def riddle_Winchester():
    rand = randint(0, 10)


    print("\nGuess the number between 0 and 100,000!\n")
    while True:
        answer = input()
        try:
            val = int(answer)
        except ValueError:
            print("you must enter an integer")
            continue
        #else:
        if (val == rand):
            print ("\nCorrect\n")
            user_input = input("> ")
            return user_input
        elif (val < rand):
            print("\nHigher\n")
        elif (val > rand):
            print("\nLower\n")
        else:
            print("Try again!")

# def main():
	# riddle_Winchester()


# if __name__ == "__main__":
    # main()
"""

###########
Puzzle Four
###########

Still to be decided:
					-Third puzzle set
					-Fourth puzzle set
					-Further clues
					-Further puzzles


"""

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




def riddle_OGT(room):
	if room['name'] == 'room_The_Old_Green_Tree':
		answer == input("I don't have eyes, but once I did see. Once I had thoughts, but now I'm white and empty.")
		filter_words()
		remove_punct()
		normalise_input()
		if answer == 'Skull':
			print("Correct")
		else:
			print('Think more halloween!')
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


def riddle_TFA(room):
	if room['name'] == 'room_The_Fat_Angel':
		print("I am the first on Earth,")
		print("The second in Heaven,")
		print("I appear two times in a week,")
		print("you can only see me once in a year, although I am in the middle to the sea.")
		answer == input("What am I?")
		filter_words()
		remove_punct()
		normalise_input()
		if answer == 'e'or 'E':
			print("Correct")
		else:
			print("Read the sentence closely")
			riddle_TFA()


"""

############
Riddle Three
###########

"""
def riddle_Winchester():
	rand = randint(0, 10)


	print("Guess the number between 0 and 100,000!")
		

	while True:
		while True:
			try:
				answer = int(input())
				break
			except ValueError:
				print("you must enter an integer")
				continue
		if (answer == rand):
			print ("Correct")
			break
		elif (answer < rand):
			print("Higher")
		elif (answer > rand):
			print("Lower")
		else:
			print("Try again!")



def main():
	riddle_Winchester()


if __name__ == "__main__":
    main()
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

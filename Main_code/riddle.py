from map import rooms
from items import *
from gameparser import *
import random
import time

"""

##########
Riddle One
##########

first part of the puzzles for the 'Old Green Tree'.

"""

def riddle_OGT():
	# if room['name'] == 'room_The_Old_Green_Tree':
    print("\nAs you turn to leave, a mysterious woman adorned with a tightly fitted skull mask steps in front of you.\n\n")
    time.sleep(1.75)
    print("\nI don't have eyes,")
    time.sleep(1.25)
    print("but once I did see.")
    time.sleep(1.25)
    print("Once I had thoughts,")
    time.sleep(1.25)
    print("but now I'm white and empty.\n\n")
    time.sleep(1.25)
    print("What am I?\n")
    answer = raw_input("> ")
    normalise_input(answer)
    
    if answer == 'skull':
        global thirdnumber
        print("Correct\n")
        print("The third digit you seek is a " + str(thirdnumber) + "\n")
        
    else:
        print('\nNot so. Look upon my face, and you shall find the answer you seek.\n')
        riddle_OGT()



"""


##########
Riddle Two
##########


"""


def riddle_TFA():
	# if room['name'] == 'room_The_Fat_Angel':
    print("#################################################")
    print("""As you look past towards the cauldron, you are greeted by... well... a fat angel.
You presume that the landlady has transfigured herself to better represent her pub.
She moves in closer and says:\n\n""")
    time.sleep(1.75)
    print("I am the first on Earth,")
    time.sleep(1.25)
    print("The second in Heaven,")
    time.sleep(1.25)
    print("I appear two times in a week,")
    time.sleep(1.25)
    print("you can only see me once in a year, although I am in the middle to the sea.\n\n")
    time.sleep(1.25)
    print("What am I?\n")
    answer = raw_input("> ")
    normalise_input(answer)
    if answer == 'e'or answer == 'E':
        global firstnumber
        print("\nBravo. The first number towards your desire is a " + str(firstnumber) + "\n")
                        
    else:
        print("\nFalse.\nListen not to the words that I speak, but to the letters therein.\n")
        riddle_TFA()


"""

############
Riddle Three
###########

"""

def riddle_Winchester():
    rand = random.randint(0, 100)
    print("""A young girl seated on the table nearest to you gets up and blocks your path.
She would be quite adorable,
were it not for the giant,
blood-stained fangs protruding from her mouth.""")
    time.sleep(1.75)
    print("\nHello Mister. I'm thinking of a number between 1 and 100, she says.\n\n")
    print("Guess the number:\n")
    time.sleep(1.25)
    while True:
        answer = raw_input("> ")
        try:
            val = int(answer)
        except ValueError:
            print("you must enter an integer\n")
            answer = raw_input("> ")
            continue
        #else:
        if (val == rand):
            global secondnumber
            print ("\nYAY! The middle number is a " + str(secondnumber) + "\n")
            break
        elif (val < rand):
            print("\nNo, silly! My number is higher\n")
        elif (val > rand):
            print("\nNo, muppet! My number is lower\n")
        else:
            print("Silly Billy... Try again!")
            

"""

############
PIN CODE GENERATOR
###########

"""
number = 0
global pin_number
pin_number =  random.randint(100,999)
numberstring = str(pin_number)
firstnumber = numberstring[0]
secondnumber = numberstring[1]
thirdnumber = numberstring[2]
print(firstnumber)
print(secondnumber)
print(thirdnumber)
# def main():


	# riddle_Winchester()


# if __name__ == "__main__":
    # main()
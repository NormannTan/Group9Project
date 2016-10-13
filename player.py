# 
# Stores variables owned by the player
#
# Add more as required
#

from items import *
from map import rooms

# Player inventory
inventory = []

# Room the player is currently in
current_room = rooms["Intro"]

# Win/Lose
victory = False
loss = False
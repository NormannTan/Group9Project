from items import *

room_Park = {
    "name": "The Park",

    "description":
    """You are stood in a park not far from your house. 
In the background is a pair of discordant noises: a car alarm and high pitched laughter, both far away. 
To the SOUTH is your house, which isn't much use without the key. 
To the NORTH is The Old Green Tree, the first, and only, bar you remember going to last night.
To the EAST is the TOWN CENTRE, maybe a clue could be found there...""",

    "exits": {"south": "Home", "east": "Town"}, # COMPLETE ME! ADD EXITS!
    
    "items": [item_biscuits, item_handbook]
}

room_The_Old_Green_Tree = {
    "name": "The_Old_Green_Tree",

    "description":
    """You are leaning agains the door of the systems managers'
room. Inside you notice Matt "MJ" John and Simon Jones. They
ignore you. To the north is the reception.""",

	"exits": {"west": "Park", "south": "Town", "east": "Off_Licence"},
    # ADD EXITS HERE!
    
    "items": []
}

room_Home = {
    "name": "Home",

    "description":
    """Your house is small and miserable, much like yourself. 
The door is locked. The park is to your NORTH.""",
	"exits": {"north": "Park"},
    # ADD EXITS HERE!
    
    "items": []
}

room_Town = {
    "name": "Town",

    "description":
    """You are standing in the Queen's Buildings parking lot.
You can go south to the COMSC reception, or east to the
general office.""",
	
	"exits": {"south": "The_Fat_Angel", "east": "The_Winchester", "west": "Park", "north": "Bar_1"},
    # ADD EXITS HERE!
    
    "items": []
}

room_Off_Licence = {
    "name": "Off Licence",

    "description":
    """You are standing next to the cashier's till at
30-36 Newport Road. The cashier looks at you with hope
in their eyes. If you go west you can return to the
Queen's Buildings.""",

	"exits": {"west": "The_Old_Green_Tree", "south": "The_Winchester"},
    # ADD EXITS HERE!
    
    "items": []
}

room_The_Winchester = {
    "name": "The_Winchester",

    "description":
    """You are standing next to the cashier's till at
30-36 Newport Road. The cashier looks at you with hope
in their eyes. If you go west you can return to the
Queen's Buildings.""",

	"exits": {"west": "Town", "south": "The_Fat_Angel", "north": "Off_Licence"},
    # ADD EXITS HERE!
    
    "items": []
}

room_The_Fat_Angel = {
    "name": "The_Fat_Angel",

    "description":
    """You are standing next to the cashier's till at
30-36 Newport Road. The cashier looks at you with hope
in their eyes. If you go west you can return to the
Queen's Buildings.""",

	"exits": {"north": "Town", "east": "The_Winchester"},
    # ADD EXITS HERE!
    
    "items": []
}

room_Intro = {
    "name": "Intro",

    "description":
    """You wake up, outside. You are surrounded by darkness. 
Around you are the empty carcasses of used beer bottles, and a half empty bottle of 38% Sidorov vodka.
You check your watch: 19:07. Have you really been asleep for 13 hours? 
Rising to your feet, you manage to faintly observe your surroundings...
You are stood in a park not far from your house. 
In the background is a pair of discordant noises: a car alarm and high pitched laughter, both far away. 
To the SOUTH is your house, and more importantly, a warm king-sized bed.""",

	"exits": {"south": "Home"},
    # ADD EXITS HERE!
    
    "items": []
}

rooms = {
    "Park": room_Park,
    "The_Old_Green_Tree": room_The_Old_Green_Tree,
    "Home": room_Home,
    "Town": room_Town,
    "Off_Licence": room_Off_Licence,
    "The_Winchester": room_The_Winchester,
    "The_Fat_Angel": room_The_Fat_Angel,
    "Intro": room_Intro,
}

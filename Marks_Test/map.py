from items import *

room_Intro = {
    "name": "Intro",

    "description":
    """You wake up, outside. You are surrounded by darkness. 
Around you are the empty carcasses of used beer bottles, and a half empty bottle of 38% Sidorov vodka.
You check your watch: 19:07. Have you really been asleep for 13 hours? 
Rising to your feet, you manage to faintly observe your surroundings...
You are stood in a park not far from your house. 
In the background is a pair of discordant noises: a car alarm and high pitched laughter, both far away. 
To the SOUTH is your house, and more importantly, a warm king-sized bed.

GO SOUTH to begin your journey.

(At any point, type "glossary" to see the list of available commands.)""",

	"exits": {"south": "House"},
        
    "items": []
}

room_House = {
    "name": "Your House",

    "description":
    """Your house is small and miserable, much like yourself.
The door is locked. 

The PARK is to your NORTH.""",
	"exits": {"north": "Park"},
        
    "items": []
}

room_Park = {
    "name": "The Park",

    "description":
    """You are stood in a park not far from your house. 
In the background is a pair of discordant noises: a car alarm and high pitched laughter, both far away. 
To the SOUTH is your HOUSE, which isn't much use without the key. 
To the NORTH is THE OLD GREEN TREE, the first, and only, bar you remember going to last night.
To the EAST is the TOWN CENTRE, maybe a clue could be found there...""",

    "exits": {"south": "House", "east": "Town", "north": "NW_Corner"},
    
    "items": []
}

room_NW_Corner_Transition = {

    "name": "NW Corner",

    "description":
    """>>>>NW Transition<<<<""",

    "exits": {"south": "Park", "east": "The_Old_Green_Tree"},
    
    "items": []
}

room_SE_Corner_Transition = {

    "name": "SE Corner",

    "description":
    """>>>>SE Transition<<<<""",

    "exits": {"North": "The_Fat_Angel", "west": "The_Winchester"},
    
    "items": []
}



room_The_Old_Green_Tree = {
    "name": "The_Old_Green_Tree",

    "description":
    """The Old Green Tree was your first port of call last night.
It is normally a warm, vibrant pub, perfect for pre-drinks.
Today, however, something is off.
Cobwebs hang from the ceiling, occupied by large spiders.
The bar is bereft of its usual patrons, instead being occupied by all manner of ghouls, goblins and ghastly creatures.
You, as the sole humanoid patron, manage to remain undetected by pulling the very best of your many ugly faces.
However cursory glances indicate that none of your belongings are here.

To the WEST is the PARK;
SOUTH of you lies the TOWN CENTRE;
EAST there is an OFF LICENCE shop you frequently patron.""",

	"exits": {"west": "NW_Corner", "south": "Town", "east": "Off_Licence"},
        
    "items": []
}



room_Town = {
    "name": "Town",

    "description":
    """"Town" is a generous term, given the unimpressive scale of the place.
But that is only at the back of your mind right now. 
As you scamper to avoid an assortment of zombies, werewolves, and what looks like mummies in the distance.

To the NORTH lies THE OLD GREEN TREE;
 to the WEST is the PARK;
 EAST leads to THE FAT ANGEL;
 and SOUTH will take you towards THE WINCHESTER.""",
	
	"exits": {"south": "The_Winchester", "east": "The_Fat_Angel", "west": "Park", "north": "The_Old_Green_Tree"},
        
    "items": []
}

room_Off_Licence = {
    "name": "Off Licence",

    "description":
    """The shop is open, but empty.
As you stumble inside, you notice that most of the usual confectionery has been replaced by spiders and eyeballs.
It's a good thing you aren't hungry.
Just as you turn to leave, you spot an old dusty WALLET out of the corner of your eye.

To the WEST is THE OLD GREEN TREE.
Heading SOUTH will take you to THE FAT ANGEL pub, which you were in last night...
... ... Probably.""",

	"exits": {"west": "The_Old_Green_Tree", "south": "The_Fat_Angel"},

    "items": [item_wallet]
}

room_The_Winchester = {
    "name": "The_Winchester",

    "description":
    """Ah, the Winchester.
Commonly known as the World's End, and with good reason.
You don't need to remember last night to know that this cesspit would have been the end of your journey.
And maybe it could be the end of your journey tonight too, as you spot a pair of KEYS lying on the far table.

From here you can journey NORTH to the TOWN CENTRE,
Or EAST to THE FAT ANGEL""",

	"exits": {"east": "SE_Corner", "north": "Town"},
    
    "items": [item_keys]
}

room_The_Fat_Angel = {
    "name": "The_Fat_Angel",

    "description":
    """The Fat Angel, so named due to its iconic and heavily-weathered statue at the front.
This bar is busy too, but the clientele are a little more rough around the edges.
There is a distinct lack of manners, and teeth.
You notice the large beer barrel that usually adorns the far corner has been replaced by a small black couldron.
Underneath it, lies a small grey object... your PHONE!

From here, WEST will lead back to the TOWN CENTRE,
NORTH will lead you to the OFF LICENCE,
SOUTH will take you to the WINCHESTER.""",

	"exits": {"south": "SE_Corner", "west": "Town", "north": "Off_Licence"},
        
    "items": [item_phone]
}





rooms = {
    "Park": room_Park,
    "The_Old_Green_Tree": room_The_Old_Green_Tree,
    "House": room_House,
    "Town": room_Town,
    "Off_Licence": room_Off_Licence,
    "The_Winchester": room_The_Winchester,
    "The_Fat_Angel": room_The_Fat_Angel,
    "Intro": room_Intro,
    "NW_Corner": room_NW_Corner_Transition,
    "SE_Corner": room_SE_Corner_Transition
}

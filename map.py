from items import *
from people import *
from puzzles import *

room_courtyard = {
    "name": "Courtyard",

    "description":
    """This is the courtyard. TODO ---""",
    # exits/people/items in room will be added using functions in game.py
    # (printed in full sentences)

    "exits": {"north": "Great Hall", "south": "Battlements"},

    "items": [],

    "people": {"lady":people_lady},

    "puzzles" : []
    
}

room_greathall = {
    "name": "Great Hall",

    "description":
    """This is the great hall. TODO ---""",

    "exits": {"west": "Throne Room", "south": "Courtyard", "east": "Battlements", "north": "Anti Room"},

    "items": [],

    "people": {"wizard":people_wizard},

    "puzzles" : []
}

room_throne = {
    "name": "Throne Room",

    "description":
    """This is the throne room. TODO ---""",

    "exits": {"east": "Great Hall"},

    "items": [],

    "people": {"king":people_king, "viceroy":people_viceroy},

    "puzzles" : []
}

room_battlements = {
    "name": "Battlements",

    "description":
    """These are the battlements. TODO ---""",

    "exits": {"west": "Great Hall", "north": "Courtyard"},

    "items": [],

    "people": {"soldier":people_soldier1, "warrior":people_soldier2},

    "puzzles" : [dice_game]
}

room_anti = {
    "name": "Anti Room",

    "description":
    """This is the anti room. TODO ---""",

    "exits": {"south": "Great Hall"},

    "items": [],

    "people": {},

    "puzzles" : []
}

room_jail = {
    "name": "Jail",

    "description":
    """This is the jail. TODO ---""",

    "exits": {},

    "items": [],

    "people": {},

    "puzzles" : []
}


rooms = {
    "Courtyard": room_courtyard,
    "Great Hall": room_greathall,
    "Throne Room": room_throne,
    "Battlements": room_battlements,
    "Anti Room": room_anti,
    "Jail": room_jail
}

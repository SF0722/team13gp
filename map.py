from items import *
from people import *

room_courtyard = {
    "name": "Courtyard",

    "description":
    """This is the courtyard. TODO ---""",
    # exits/people/items in room will be added using functions in game.py
    # (printed in full sentences)

    "exits": {"north": "Great Hall", "south": "Battlements"},

    "items": [],

    "people": {"lady":people_lady}
}

room_greathall = {
    "name": "Great Hall",

    "description":
    """This is the great hall. TODO ---""",

    "exits": {"west": "Throne Room", "south": "Courtyard", "east": "Battlements", "north": "Anti Room"},

    "items": [],

    "people": {"wizard":people_wizard}
}

room_throne = {
    "name": "Throne Room",

    "description":
    """This is the throne room. TODO ---""",

    "exits": {"east": "Great Hall"},

    "items": [],

    "people": {"king":people_king, "viceroy":people_viceroy}
}

room_battlements = {
    "name": "Battlements",

    "description":
    """These are the battlements. TODO ---""",

    "exits": {"west": "Great Hall", "north": "Courtyard"},

    "items": [],

    "people": {"soldier1":people_soldier1, "soldier2":people_soldier2}
}

room_anti = {
    "name": "Anti Room",

    "description":
    """This is the anti room. TODO ---""",

    "exits": {"south": "Great Hall"},

    "items": [],

    "people": {}
}

room_jail = {
    "name": "Jail",

    "description":
    """This is the jail. TODO ---""",

    "exits": {},

    "items": [],

    "people": {}
}


rooms = {
    "Courtyard": room_courtyard,
    "Great Hall": room_greathall,
    "Throne Room": room_throne,
    "Battlements": room_battlements,
    "Anti Room": room_anti,
    "Jail": room_jail
}

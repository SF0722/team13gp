item_goldgoblet = {
    "id": "chalice",

    "name": "a chalice",

    "description":
    """A Golden Goblet *TODO-- """,

    "mass": 0   
}

item_goblet = {
    "id": "goblet",

    "name": "a goblet",

    "description":
    "A standard wooden goblet. It has split and is pretty much unusable.",

    "mass": 0
}

item_knife = {
    "id": "knife",

    "name": "a knife",

    "description":
    "A hunting knife.",

    "mass": 0
}

item_oldboot = {
    "id": "boot",

    "name": "a boot",

    "description": "A smelly old boot, gross!",

    "mass": 0
}

item_sword = {
    "id": "sword",
    
    "name": "a sword",

    "description": "A sharp steel shortsword.",

    "mass": 0
}

item_potionbook = {
    "id": "book",
    
    "name": "a book",

    "description": "A book of potions *TODO-- ",

    "mass": 0
}

item_waterboot = {
	"id": "boot",
	
	"name": "a boot full of water",
	
	"description": "A smelly old boot, filled with water.",
	
	"mass": 0
	
}
	
def inter_fountain(item_id):
	from player import inventory
	if item_id == "oldboot":
		inventory.remove[item_oldboot]
		inventory.append[item_waterboot]
		print("You fill the old boot up with water.")


object_fountain = {
	"id": "fountain",
	
	"description": "An ornate water feature",
	
	"interaction": inter_fountain
}
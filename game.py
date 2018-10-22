#!/usr/bin/python3
import time
from random import randint

from map import rooms
from player import *
from items import *
from gameparser import *
from people import *
       

def print_inventory_items(items):
    """This function takes a list of inventory items and displays it in the format
    shown in the doctest below.

    >>> print_inventory_items([item_goldgoblet, item_goblet, item_oldboot, item_knife])
    You have a chalice, along with a goblet, a boot and a knife.

    >>> print_inventory_items([item_goldgoblet, item_goblet, item_oldboot])
    You have a chalice, along with a goblet and a boot.

    >>> print_inventory_items([item_goldgoblet])
    You have a chalice.

    """

    inv_str = ""    # concatenated string
    inv_count = 0   # number of inventory items
    
    for i in items :
        inv_count += 1

        if inv_count == 1 :
            # start of sentence
            inv_str += "You have " + i["name"]

        elif inv_count == 2 :
            # connector phrase to additional item
            inv_str += ", along with " + i["name"]
            
        else :
            # from this point, all other items are separated with commas
            inv_str += ", " + i["name"]
            

    if inv_str != "" :
        if inv_count <= 2 :
            # end sentence with full stop
            inv_str += "."

        else :
            # for items separated by commas, an 'and' is inserted before the last item for fluid reading
            inv_str = inv_str.rpartition(",")[0] + " and" + inv_str.rpartition(",")[2] + "."

        print(inv_str)



def print_exit(direction, leads_to):
    """Prints available exits in full sentences in one of three randomly-chosen formats.

    For example:
    The (place) lies to the (direction).      -or-
    To the (direction) is the (place).        -or-
    There is a (place) to the (direction).

    The Battlements is the only plural room name. Therefore, the following format is used:
    The battlements are to the (direction).

    """
    
    if leads_to.lower() == "battlements" :
        # special case for battlements room (see documentation)
        return "The " + leads_to.lower() + " are to the " + direction + ". "

    else :
        # choose one of three formats
        sentence_choice = randint(1, 3)

        if sentence_choice == 1 :
            return "The " + leads_to.lower() + " lies to the " + direction + ". "

        elif sentence_choice == 2 :
            return "To the " + direction + " is the " + leads_to.lower() + ". "

        elif sentence_choice == 3 :
            return "There is a " + leads_to.lower() + " to the " + direction + ". "



def print_people(people):
    """This function takes a list of people in the current room and displays it in the format
    shown in the doctest below.

    >>> print_people([people_soldier1, people_soldier2])
    In the room, a soldier and a warrior are present.

    >>> print_people([people_lady])
    In the room, the lady of the court is present.

    >>> print_people([people_king, people_lady, people_soldier2])
    In the room, the king, the lady of the court and a warrior are present.

    """

    ppl_str = ""    # concatenated string
    ppl_count = 0   # number of people in room
    
    for i in people :
        ppl_count += 1
        
        if ppl_count == 1 :
            # start of sentence
            ppl_str += "In the room, " + current_room["people"][i]["name"]
            
        else :
            # from this point, all other items are separated with commas
            ppl_str += ", " + current_room["people"][i]["name"]
            

    if ppl_str != "" :
        
        if ppl_count != 1 :
            # for items separated by commas, an 'and' is inserted before the last item for fluid reading
            ppl_str = ppl_str.rpartition(",")[0] + " and" + ppl_str.rpartition(",")[2] + " are present."

        else :
            # end sentence with full stop
            ppl_str += " is present."
            
        print(ppl_str)
        
    

def print_room(room):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in the following format...

    _____________                  _______________

    ~ COURTYARD ~       -or-       ~ BATTLEMENTS ~
    _____________                  _______________
    
    ... where the underscores match the length of the room name.
    Other details such as the description of the room are printed afterwards.

    """
    
    # Display room name
    print("_" * (len(room["name"]) + 4))
    print()
    print("~ " + room["name"].upper() + " ~")
    print("_" * (len(room["name"]) + 4))
    
    # Display room description
    print()
    print(room["description"])
    print()

    # Print exits in full sentences
    exit_str = ""
    
    # Iterate over available exits
    for direction in room["exits"]:
        # Print the exit name and where it leads to
        exit_str += print_exit(direction, exit_leads_to(room["exits"], direction))

    if exit_str != "" :
        # Print the string
        print(exit_str)

        

def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. For example:

    >>> exit_leads_to(rooms["Courtyard"]["exits"], "south")
    "Battlements"
    >>> exit_leads_to(rooms["Throne Room"]["exits"], "east")
    "Great Hall"

    """
    
    return rooms[exits[direction]]["name"]



def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:

    >>> is_valid_exit(rooms["Courtyard"]["exits"], "south")
    True
    >>> is_valid_exit(rooms["Throne Room"]["exits"], "up")
    False
    >>> is_valid_exit(rooms["Great Hall"]["exits"], "north")
    False
    >>> is_valid_exit(rooms["Anti Room"]["exits"], "south")
    True
    """
    
    return chosen_exit in exits



def is_valid_person(people, chosen_person):
    """This function checks the chosen person is in the room.

    >>> is_valid_person(rooms["Throne Room"]["people"], "king")
    True
    >>> is_valid_person(rooms["Throne Room"]["people"], "lady")
    False
    
    """

    return chosen_person in people



def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """

    global current_room
    
    if is_valid_exit(current_room["exits"], direction) :
        current_room = move(current_room["exits"], direction)
        return True

    else :
        print("You cannot go there.")
        return False



def execute_take(item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """

    found_item = False
    
    for i in current_room["items"] :
        
        if i["id"] == item_id :
            inventory.append(i)
            current_room["items"].remove(i)

            print("You now possess the " + item_id + ".")
            print()
            time.sleep(0.5)

            found_item = True
            break

        
    if found_item == False :
        print("You cannot take that.")  


def execute_drop(item_id):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """

    found_item = False
    
    for i in inventory :
        if i["id"] == item_id :
            current_room["items"].append(i)
            inventory.remove(i)

            print("You no longer hold the " + item_id + ".")
            print()
            time.sleep(0.5)

            found_item = True
            break
        
    if found_item == False :
        print("You cannot drop that.")    



def execute_talk(people_id):
    """This function takes a people_id as an argument and begins a conversation
    with the person."""
    
    if is_valid_person(current_room["people"], people_id) :
        person_conv = current_room["people"][people_id]["conversation"]

        print(person_conv["opening"])
        input("Press ENTER to continue...")
        
        print("\nYou can ask...")
        qcount = 0

        if not person_conv["questions"] == [] :
            
            for q in range(0, len(person_conv["questions"])) :
                print("Input %d to ask '%s'" % (q+1, person_conv["questions"][q]))
                qcount += 1

            while True :
                try :
                    qask = int(input("\n> "))

                    if qask <= qcount and qask > 0 :
                        print(person_conv["responses"][qask-1])
                        input("Press ENTER to continue...")
                        break

                    else :
                        print("You cannot ask that.")

                except :
                    print("Type a number from the list of questions.")
        
    else :
        print("This person isn't here.")

def execute_use(item_id, object_id):
	#check if item is in inventory
	#check if object is in room
	#run interaction code
	found_item = False
	found_object = False
	a = None
	b = None
	for i in inventory :
		if i["id"] == item_id :
			found_item = True
			a = i
		if i["id"] == object_id :
			found_object = True
			b = i
	for i in current_room["objects"]:
		if i["id"] == object_id:
			found_object = True
			b = i
	if found_item == True and found_object == True:
		if b["interaction"] != None:
			funct_run = b["interaction"]
			funct_run(item_id)
		else:
			print("Nothing interesting happens.")
	else:
		print("You cannot do that")
			
def execute_examine(object):
	#check if object is in inventory/room
	#return 'description' from the objects properties
	#print the description
	found_object = False
	a = None
	for i in inventory :
		if i["id"] == object:
			found_object = True
			a = i
	if found_object == False:
		for i in current_room["objects"]:
			if i["id"] == object:
				found_object = True
				a = i
	if found_object:
		print(a["description"])
		
	else:
		print("You cannot do that.")

def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command), executes the relevant function, supplying the second word
    as the argument.

    Note: This function will only return False when the player changes room.
    """

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            if execute_go(command[1]) :
                return False      
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

    elif command[0] == "talk":
        if len(command) > 1:
            execute_talk(command[1])
        else:
            print("Talk to whom?")
     
    elif command[0] == "use":
        if len(command) > 1:
            execute_use(command[1], command[2])
        else:
            print("You cannot do that.")
			
    elif command[0] == "examine":
        if len(command) > 1:
            execute_examine(command[1])
        else:
            print("Examine what?")
    else:
        print("This makes no sense.")



def menu(exits, room_items, inv_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.

    """

    print()
    print("What do you want to do?")

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input



def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:

    >>> move(rooms["Courtyard"]["exits"], "south") == rooms["Battlements"]
    True
    >>> move(rooms["Great Hall"]["exits"], "west") == rooms["Courtyard"]
    False
    """

    # Next room to go to
    return rooms[exits[direction]]



# This is the entry point of our program
def main():

    print("Welcome!")
    time.sleep(0.5)
    
    # Main game loop
    while True:
        
        # Display game status (room description, inventory etc.)
        print_room(current_room)
        print_inventory_items(inventory)
        print_people(current_room["people"])

        while True :
            # Execute the player's command and only repeat the above few lines of
            # code if the function returns True (see function documentation for more)
            command = menu(current_room["exits"], current_room["items"], inventory)
            
            if execute_command(command) == False :
                break
        

# If running as script, run main()
if __name__ == "__main__":
    main()




import random
def dice_game(): #code for celo game from https://code.sololearn.com/cjQ6V2Aj2rJk/#py

    def cee_lo_player():
        combo = roll()
        win = [4,5,6]
        loss = [1,2,3]
        w=9
        l=0
        print("You rolled %s" %combo[0] + "-%s" %combo[1] + "-%s" %combo[2])
        if combo==win:
            print("You rolled Cee-lo!")
            return w
        elif combo==loss:
            print("You rolled 123!")
            return l
        elif combo[0]==combo[1]==combo[2]:
            print("You rolled TRIP %s's!" %combo[0])
            return combo[0]
        elif combo[0]==combo[1] or combo[1]==combo[2]:
            if combo[0]==combo[1]:
                print("You rolled a PAIR of %s's!" %combo[1])
                print("Your number is %s!" %combo[2])
                return combo[2]
            elif combo[1]==combo[2]:
                print("You rolled a PAIR of %s's!" %combo[1])
                print("Your number is %s!" %combo[0])
                return combo[0]
        else:
            return cee_lo_player()


    def cee_lo_Soldier():
        combo = roll()
        win = [4,5,6]
        loss = [1,2,3]
        w=9
        l=0
        print("Soldier rolled %s" %combo[0] + "-%s" %combo[1] + "-%s" %combo[2])
        if combo==win:
            print("Soldier rolled Cee-lo!")
            return w
        elif combo==loss:
            print("Soldier rolled 123!")
            return l
        elif combo[0]==combo[1]==combo[2]:
            print("Soldier rolled TRIP %s's!" %combo[0])
            return combo[0]
        elif combo[0]==combo[1] or combo[1]==combo[2]:
            if combo[0]==combo[1]:
                print("Soldier rolled a PAIR of %s's!" %combo[1])
                print("Soldier number is %s!" %combo[2])
                return combo[2]
            elif combo[1]==combo[2]:
                print("Soldier rolled a PAIR of %s's!" %combo[1])
                print("Soldier number is %s!" %combo[0])
                return combo[0]
        else:
            return cee_lo_Soldier()

    def roll():
        dice1 = random.randrange(1,7,1)
        dice2 = random.randrange(1,7,1)
        dice3 = random.randrange(1,7,1)
        combo = [dice1,dice2,dice3]
        return sorted(combo)

    print("Rollin' the dice...\n")
    player = cee_lo_player()
    print("")
    Soldier = cee_lo_Soldier()
    print("")
    print("You: %s" %player)
    print("Soldier: %s" %Soldier)
    if player > Soldier:
        print("YOU WIN!")
        from player import inventory
        from items import item_money

        inventory.append(item_money)
        print("Soldier: 'Here take my gold.''") #debugging step
    elif Soldier > player:
        print("YOU LOSE!")
    elif player == Soldier:
        print("DRAW!")

puzzles = {"dice":dice_game}

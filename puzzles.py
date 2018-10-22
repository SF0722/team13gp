

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


    def cee_lo_cpu():
        combo = roll()
        win = [4,5,6]
        loss = [1,2,3]
        w=9
        l=0
        print("CPU rolled %s" %combo[0] + "-%s" %combo[1] + "-%s" %combo[2])
        if combo==win:
            print("CPU rolled Cee-lo!")
            return w
        elif combo==loss:
            print("CPU rolled 123!")
            return l
        elif combo[0]==combo[1]==combo[2]:
            print("CPU rolled TRIP %s's!" %combo[0])
            return combo[0]
        elif combo[0]==combo[1] or combo[1]==combo[2]:
            if combo[0]==combo[1]:
                print("CPU rolled a PAIR of %s's!" %combo[1])
                print("CPU number is %s!" %combo[2])
                return combo[2]
            elif combo[1]==combo[2]:
                print("CPU rolled a PAIR of %s's!" %combo[1])
                print("CPU number is %s!" %combo[0])
                return combo[0]
        else:
            return cee_lo_cpu()

    def roll():
        dice1 = random.randrange(1,7,1)
        dice2 = random.randrange(1,7,1)
        dice3 = random.randrange(1,7,1)
        combo = [dice1,dice2,dice3]
        return sorted(combo)
     
    print("Rollin' the dice...\n")
    player = cee_lo_player()
    print("")
    cpu = cee_lo_cpu()
    print("")
    print("You: %s" %player)
    print("Cpu: %s" %cpu)
    if player > cpu:
        print("YOU WIN!")
        from player import inventory
        from items import item_money
        
        inventory.append(item_money)
        print(inventory) #debugging step
    elif cpu > player:
        print("YOU LOSE!")
    elif player == cpu:
        print("DRAW!")

puzzles = {"dice":dice_game}

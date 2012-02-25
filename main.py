# Copyrigth 2012 - Itxaka Serrano Garcia <itxakaserrano@garciaperez.net>


version = 0.5
status = "Beta"


print("______        _    _                   ")
print("| ___ \      | |  | |                  ")
print("| |_/ /_   _ | |_ | |__    ___   _ __  ")
print("|  __/| | | || __|| '_ \  / _ \ | '_ \ ")
print("| |   | |_| || |_ | | | || (_) || | | |")
print("\_|    \__, | \__||_| |_| \___/ |_| |_|")
print("        __/ |                          ")
print("       |___/  By Itxaka Serrano Garcia ")
print("            _                     _                           ")
print("           | |                   | |                          ")
print("  __ _   __| |__   __ ___  _ __  | |_  _   _  _ __  ___  ___  ")
print(" / _` | / _` |\ \ / // _ \| '_ \ | __|| | | || '__|/ _ \/ __| ")
print("| (_| || (_| | \ V /|  __/| | | || |_ | |_| || |  |  __/\__ \ ")
print(" \__,_| \__,_|  \_/  \___||_| |_| \__| \__,_||_|   \___||___/ ")



# imports

import random
import os
import time


# progress bar
# Output example: [=======   ]
def progress():
    marks = experience
    spaces =  10 - experience
    loader = "[" + ("=" * int(marks)) + (" " * int(spaces)) + "]" 
    print ("Experience"+loader)
    print ("Level:",player_level)
    print ("Health=",health)
    print ("Power=",power)
    print ("Magic=",magic)
 
# check if the player has leveled up
def check_levelup():
    global experience, player_level, health, power, magic, health_level
    if experience >= 10:
        player_level = player_level + 1
        print ("\nLevel up! You are level",player_level)
        experience = 0
        health = health + 2
        power = power + 2
        magic = magic + 1
        health_level = health_level + 2
    else:
        pass

# how should I check max health across the game? Some pseudocode here
#def max_health(x):
#   role.health + health_gained_by_level_up = max_health
#   if health > max_health:
#       health = max health
#   else:
#       pass
# I have to keep calling max_health() on the battle() fuction and potion event. Also I need to track how much did health increased during all level ups

# create a fuction to clear the screen which work across all os
def clear_screen():
    clear = ""
    if os.name == "posix":
        clear = "clear"
    elif os.name in ("nt","ce","dos"):
        clear = "cls"
    return clear

# function to choose a name
def choose_name():
    global name
    name = ""
    tempvar = 1
    while tempvar == 1:
        name = input("\n\nWhat is your name?\n")
        print("\nThe name you choose is ",name)
        change_name = input("\n\nDo you want to change your name? (y/n)")
        if (change_name == "n") or (change_name == "N"):
            tempvar = 0
        else:
            tempvar = 1

# function to choose a role
def choose_role():
    global role, role_name, health, power, magic, inventory
    print("\n")
    print("         1-Warrior        2-Bard           3-Mage")
    print("           -----           -----            -----")
    print("Health       8               6                4")
    print("Power        7               6                5")
    print("Magic        2               6                9")
    while role not in (1,2,3):
        role = int(input("\n\nChoose your role number (1,2 or 3)"))
    if role == 1:
        role_name = "Warrior"
        health = 15
        power = 6
        magic = 2
        inventory.append("Sword")
        print ("arrived at first if witht his values:",health,power,magic)
    elif role == 2:
        role_name = "Bard"
        health = 9
        power = 4
        magic = 6
        inventory.append("Lire")
    elif role == 3:
        role_name = "Mage"
        health = 8
        power = 3
        magic = 9
        inventory.append("Staff")

# fuction for the battles
def battle(enemy):
    print ("\nYou encounter a", enemy)
    global health, experience,game_on
    if enemy == "skeleton":
        enemy_health = 12 + player_level
        enemy_attack = 3 + player_level
        enemy_info = "Skeletons have a lot of health and they can kill you almost in one hit, watch out"      
    elif enemy == "slime":
        enemy_health = 4 + player_level
        enemy_attack = 1 + player_level
        enemy_info = "Slimes are pretty boring. They have almost no health and they hit really low"
    elif enemy == "bat":
        enemy_health = 8 + player_level
        enemy_attack = 2 + player_level
        enemy_info = "Bats have moderate life but they hit low. They have a random chance of dodging your attacks"
    elif enemy == "dragon":
        enemy_health = 30 + player_level
        enemy_attack = 5 + player_level
        enemy_info = "Run, you fool!"
    while (enemy_health > 0) and (health > 0):
        print ("What do you want to do? 1-fight, 2-potion, 3-info about the enemy, 4-run")
        choice = input(">")
        attack_list = [power,power,power,power,power/2,power+2]
        enemy_attack_list= [enemy_attack,enemy_attack,enemy_attack,enemy_attack,enemy_attack/2,enemy_attack+2]
        attack = int(random.choice(attack_list))
        enemy_attack_temp = int(random.choice(enemy_attack_list))
        if choice == "1":
            print ("\nYou hit the enemy for",attack,"damage")
            enemy_health = enemy_health - attack
            print ("Enemy hits you for",enemy_attack_temp,"damage")
            health = health - enemy_attack_temp      
            print ("\nyour health=",health," Enemy health=",enemy_health)
        elif choice == "2":
            take_potion()
        elif choice == "3":
            display_info = [enemy_info,"\nYou failed into your assasement of the enemy..."]
            print(random.choice(display_info))
        elif choice == "4":
            print ("\nYou run like a coward....")
            experience = experience - 1
            enemy_health = 0
            time.sleep(3)
            os.system(clear_screen())
    if enemy_health <= 0:
        print ("You defeated the",enemy)
        if enemy == "skeleton":
            experience = experience + 3
        elif enemy == "slime":
            experience = experience + 1
        elif enemy == "bat":
            experience = experience + 2
        elif enemy == "dragon":
            experience = experience + 6
        input("Press any key to continue")
    elif health <= 0:
        print ("You were defeated by a simple",enemy,".What a shame...")
        input("Press any key to exit")
        game_on = 999
    time.sleep(2)
    os.system(clear_screen())
     
def take_potion():
    global inventory,health
    if "potion" in inventory:
        inventory.remove("potion")
        health = health+10
    else:
        print ("\nYou don't have any potion")
     
def move():
    global look_count
    look_count = 0
    pass

# in the look fuction we include the random chance of having to battle, getting a potion or finding a chest
# should be limited to 2 events on each room, but there are no rooms yet.
def look():
    look_list = ["skeleton","potion","slime","chest","bat","special"] # events that can happen
    special_list = ["","","","","","","","","","","","","","","","","","","","","","","dragon"] # special list. We don't want special to be common rigth?
    chest_list = ["","","","","","","","","","","","","","","","","","","","","","","","potion","SteelBlade","Staff of Kings","Lire of the Tempest"] # chest list, almost empty so the chance of getting something are low
    look_random = random.choice(look_list) # randomize the event that happens when you look
    if look_random == "skeleton":
        battle("skeleton")
    elif look_random == "potion":
        print ("\nYou got a potion!")
        return inventory.append("potion") # add a potion to the inventory
    elif look_random == "slime":
        battle("slime")
    elif look_random == "bat":
        battle("bat")
    elif look_random == "chest":
        print("\nYou encounter a chest, you open it and find...")
        time.sleep(2) # sleep 2 seconds, we want some suspense
        chest_get = random.choice(chest_list) # randomize the choice from the list above
        if chest_get == "":
            print("...nothing") # You get nothing, good day sir!
        else:
            print("...",chest_get)
            return inventory.append(chest_get) # we add the item to the inventory   
    elif look_random == "special":
        print("\nSpecial event!")
        time.sleep(2)
        special = random.choice(special_list)
        if special == "":
            print("Nothing happens...")
        else:
            print("\nUh oh, you encountered a dragon!")
            battle("dragon")

            

        

        
 # PROGRAM START!       

# Set the variables from the start
count_rest = 0 # to count the number of times the player has rest and gained health. Recover chances by battling
game_on = 0 # to start the main fuction. game_on = 999 means end of the game
player_level= 0
experience = 0
look_count = 0
role = 0
role_name = ""        
health = 0
power = 0
magic = 0
inventory = []
health_level = 0

# Call player name fuction and player role function so we can get a character sheet
choose_name()
choose_role()

os.system(clear_screen())
    
print ("\n\n\n\tWelcome to the wonderful world of Python Adventures", name,"!!!")
print ("\n\n\n\tI can see that you choosed to be a", role_name,". Good choice!\n")

    

while health >= 0 and game_on != 999:
    check_levelup()
    option = input("\noptions: 1-move, 2-look, 3-rest, 9-stats, 99-inventory, 999-quit game\n>")
    if option == "1":
        move()
    elif option == "2":
        if look_count < 2:
            look()
            look_count = look_count + 1
        else:
            print ("\nThere is nothing else here")
    elif option == "3":
        if count_rest < 3:
            health = health + 3
            count_rest = count_rest + 1
            print("\nYou have only",3 - count_rest, "rests left")
        else:
            print("\nYou could only rest 3 times, battle enemies to recover rest chances")
    elif option == "9":
        os.system(clear_screen())
        progress()
    elif option == "99":
        os.system(clear_screen())
        print (inventory)
    elif option == "999":
        game_on = 999
        health = 0
#    elif option == "6":
#        experience = experience +1

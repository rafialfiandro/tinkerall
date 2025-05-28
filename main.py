import cmd
import textwrap
import sys
import os
import time
import random
import msvcrt

screen_width = 100

# Function to clear screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Player Definition
class player:
    def __init__(self):
        self.name = ''
        self.lvl = 1
        self.hp = 20
        self.mp = 0
        self.attack = 10
        self.status_effects = []

# Enemy Class Definition
class enemy:
    def __init__(self, name, health, attack, loot, chance):
        self.name = name
        self.hp = health
        self.att = attack
        self.loot = loot
        self.status_effects = []
        self.chance = chance
    
# Making a list of enemies


goblin = enemy("Goblin", 5, 5, ["Gold"], [100])
minotaur = enemy("Minotaur", 10, 5, ["Gold", "Minotaur Horn"], [75,25])
skeleton = enemy("Skeleton", 10, 6, ["Bone Fragment", "Rusty Sword"], [70, 30])
orc = enemy("Orc", 10, 9, ["Gold", "Orc Axe", "Orc Tooth"], [50, 30, 20])
dark_knight = enemy("Dark Knight", 10, 20, ["Gold", "Dark Crystal", "Cursed Blade"], [40, 30, 30])
enemies = [goblin, minotaur,skeleton,orc,dark_knight]

    
# Enemy Encounter Function    
def enemy_encounter():
    
    clear_screen()
    
    enemy = random.choice(enemies)
    action = None
    flee = False
    playerTurn = True
    enemyDefeat = False
    playerDefeat = False
    
    print("An enemy encounter!")
    
    while enemyDefeat == False or playerDefeat == False or flee == False:
        
        if enemy.hp <= 0:
            enemyDefeat = True
            break
        elif mainPlayer.hp <= 0:
            playerDefeat = True
            break
        
        if playerTurn == True:
            print('Enemy:', enemy.name)
            print('HP:', enemy.hp)
            print('What would you like to do?')
            print('[1] Attack')
            print('[2] Flee')
            print('[3] Check Stats')
            
            while action not in ['1','2', '3']:
                action = input("> ")
            
            if action == '1':
                clear_screen()
                enemy.hp -= mainPlayer.attack
                print("Player did", mainPlayer.attack, "damage to", enemy.name)
                playerTurn = False
                action = '0'
                msvcrt.getch()
            elif action == '2':
                diceRoll = random.randint(75,100) # Remember to reset
                if diceRoll < 75:
                    print(diceRoll)
                    print('succesfully fleed!')
                    flee = True
                    msvcrt.getch()
                    break
                else:
                    print('you were not able to escape')
                    action = None
                    playerTurn = False
                    msvcrt.getch()
            elif action == '3':
                clear_screen()
                print("HP:", mainPlayer.hp)
                print("Attack:", mainPlayer.attack)
                action = '0'
                msvcrt.getch()
                clear_screen()
                continue
        else:
            clear_screen()
            print("The enemy attacks you for", enemy.att, "damage")
            mainPlayer.hp -= enemy.att
            playerTurn = True
            msvcrt.getch()
    
    if enemyDefeat == True:
        print("Enemy defeated!")
        print("")
        drop = random.choices(enemy.loot, weights = enemy.chance, k=1)[0]
        print("It dropped ", drop,"!", sep='')
        msvcrt.getch()
        game_start()
    elif playerDefeat == True:
        print("You have been defeated")
        msvcrt.getch()
        title_screen()
        
    
        
def game_start():
    clear_screen()
    option = None
    print("What do you want to do?")
    print("[1] Enter Dungeon")
    print("[2] Return to Main Menu")
    
    option = input("> ")
    
    if option not in ['1','2', None]:
        option = None
        game_start()
    
    if option == '1':
        enemy_encounter()
    elif option == '2':
        title_screen()
        

# Title Screen Function
def title_screen():
    
    clear_screen()
    
    option = None
    
    print("          ==========================")
    print("                   TINKERALL        ")
    print("          ==========================")
    print()
    print("             [1] Play Game")
    print("             [2] Credits")
    print("             [3] Quit")
    print()
    print("          ==========================")
    
    option = input("> ")
    
    if option not in ['1','2','3',None]:
        option = None
        title_screen()
    
    if option == "1":
        game_start()
        #print("game starts")
    elif option == "2":
        #credits()
        print("made by me")
        print("press any key to return to main menu")
        msvcrt.getch()
        title_screen()
    elif option == "3":
        sys.exit()
     
# Call in-game Objects   
mainPlayer = player()

title_screen()
import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

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
    
    enemy = random.choice(enemies)
    action = None
    flee = False
    playerTurn = True
    
    print("An enemy encounter!")
    
    while enemy.hp > 0 or flee != True:
        
        if enemy.hp <= 0:
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
                enemy.hp -= mainPlayer.attack
                playerTurn = False
                action = '0'
            elif action == '2':
                diceRoll = random.randint(75,100)
                if diceRoll < 75:
                    print(diceRoll)
                    print('succesfully fleed!')
                    #flee = True
                    break
                else:
                    print('you were not able to escape')
                    action = '0'
                    playerTurn = False
            elif action == '3':
                print("HP:", mainPlayer.hp)
                print("Attack:", mainPlayer.attack)
                action = '0'
                continue
        else:
            print("The enemy attacks you for", enemy.att, "damage")
            mainPlayer.hp -= enemy.att
            playerTurn = True
    
    print("Enemy defeated!")
    
    drop = random.choices(enemy.loot, weights = enemy.chance, k=1)[0]
    print("It dropped ", drop,"!", sep='')
    
        
def game_start():
    option = None
    print("What do you want to do?")
    print("[1] Enter Dungeon")
    print("[2] Return to Main Menu")
    
    while option not in ["1", "2"]:
        option = input()
        
        if option == '1':
            enemy_encounter()
        elif option == '2':
            title_screen()

# Title Screen Function
def title_screen():
    
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
    
    while(option not in ['1', '2', '3']):
        option = input("> ")
    
    if option == "1":
        game_start()
        #print("game starts")
    elif option == "2":
        #credits()
        print("made by me")
    elif option == "3":
        print('Thank you for playing!')
        sys.exit()
    else:
        print("input not recognized")
     
# Call in-game Objects   
mainPlayer = player()

title_screen()


        
        
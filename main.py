import sys
import os
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
        self.maxhp = 20
        self.hp = 15
        self.mp = 0
        self.attack = 10
        self.status_effects = []
        self.inventory = {}
        self.gold = 100

# Call in-game Objects   
mainPlayer = player()

# Declare Master List of Items and Sell Values
itemList = {
    # Potions
    "Potion": 30,
    "Antidote": 20,
    
    # Weapons
    "Wooden Sword": 30,
    "Iron Dagger": 100,
    
    # Armor / Gear
    "Leather Armor": 30,
    "Bronze Shield": 40,
}

# Declare item effects
def use_item(used):
    
    print("You used", used)
    print()
    
    if used == "Potion":
        mainPlayer.hp += 10
        if mainPlayer.hp > mainPlayer.maxhp:
            mainPlayer.hp = mainPlayer.maxhp
        print("Your HP is filled by 10!")
        msvcrt.getch()

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
def enemy_creation():
    def create_goblin():
        return enemy("Goblin", 5, 5, ["Gold"], [100])

    def create_minotaur():
        return enemy("Minotaur", 10, 5, ["Gold", "Minotaur Horn"], [75,25])

    def create_skeleton():
        return enemy("Skeleton", 10, 6, ["Bone Fragment", "Rusty Sword"], [70, 30])

    def create_orc():
        return enemy("Orc", 10, 9, ["Gold", "Orc Axe", "Orc Tooth"], [50, 30, 20])
    
    def create_dark_knight():
        return enemy("Dark Knight", 10, 20, ["Gold", "Dark Crystal", "Cursed Blade"], [40, 30, 30])
    
    return [create_goblin, create_minotaur, create_skeleton, create_orc, create_dark_knight]

enemies = enemy_creation()

def check_inv():
    
    print("Inventory:")
    print()
    
    for i in mainPlayer.inventory:
        print(i, "x", mainPlayer.inventory.get(i))

# Check stats func  
def check_stats():
    print("HP:", mainPlayer.hp)
    print("Attack:", mainPlayer.attack)
    print("Gold:", mainPlayer.gold)

usable_items = ['Potion', 'Antidote']

# Enemy Encounter Function    
def enemy_encounter():
    
    clear_screen()
    
    enemy = random.choice(enemies)()
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
            print(action)
            print('Enemy:', enemy.name)
            print('HP:', enemy.hp)
            print('What would you like to do?')
            print('[1] Attack')
            print('[2] Flee')
            print('[3] Check Stats')
            print("[4] Use Items")
            
            while action not in ['1','2', '3', '4']:
                action = input("> ")
            
            if action == '1':
                clear_screen()
                enemy.hp -= mainPlayer.attack
                print("Player did", mainPlayer.attack, "damage to", enemy.name)
                playerTurn = False
                action = '0'
                print()
                print("Press any button to continue")
                msvcrt.getch()
            elif action == '2':
                diceRoll = random.randint(0,100) # Remember to reset
                if diceRoll < 75:
                    #print(diceRoll)
                    print('succesfully fleed!')
                    flee = True
                    print()
                    print("Press any button to continue")
                    msvcrt.getch()
                    game_start()
                    #break
                else:
                    print('you were not able to escape')
                    action = None
                    playerTurn = False
                    print()
                    print("Press any button to continue")
                    msvcrt.getch()
                    
            elif action == '3':
                clear_screen()
                check_stats()
                
                print()
                print("Press any button to continue")
                msvcrt.getch()
                
                action = '0'
                continue
            
            elif action =='4':
                
                itemInp = None
                
                check_inv()
                
                print('[1] Go Back')
                print()
                print("Enter the name of the item you want to use")
                
                while itemInp not in usable_items and itemInp != '1':
                    itemInp = input("> ")
                
                if itemInp == "1":
                    clear_screen()
                    itemInp = None
                    
                elif itemInp in usable_items:
                    clear_screen()
                    use_item(itemInp)
                    itemInp = None
                
                action = '0'
                continue
                
        else:
            clear_screen()
            print("The enemy attacks you for", enemy.att, "damage")
            mainPlayer.hp -= enemy.att
            playerTurn = True
            print()
            print("Press any button to continue")
            msvcrt.getch()
    
    if enemyDefeat == True:
        clear_screen()
        print("Enemy defeated!")
        print("")
        drop = random.choices(enemy.loot, weights = enemy.chance, k=1)[0]
        print("It dropped ", drop,"!", sep='')
        
        if drop == "Gold":
            mainPlayer.gold += 1
        elif drop not in mainPlayer.inventory:
            mainPlayer.inventory[drop] = 1
        else:
            mainPlayer.inventory[drop] += 1
        
        enemyDefeat = False
        
        print()
        print("Press any button to continue")
        msvcrt.getch()
        game_start()
        
    elif playerDefeat == True:
        clear_screen()
        print("You have been defeated")
        print()
        print("Press any button to continue")
        playerDefeat = False
        msvcrt.getch()
        title_screen()

# Shopkeepers Inventory
shopInventory = {
    "Potion": 3,
    "Wood Sword": 1,
    "Leather Armor": 1
}

# Shop Mechanics
def shop():
    
    clear_screen()
    
    option = None
    
    print("Shopkeeper: What can I do you for laddie?")
    print()
    print("[1] Buy")
    print("[2] Sell")
    print("[3] Go Back")
    print()
    
    while option not in ['1', '2', '3']:
        option = input("> ")
        
        if option == '1':
            print("Shopkeeper: Well then let me show you my wares!")
            print()
            
            listNum = 1
            
            for i in shopInventory:
                
                if(shopInventory.get(i) > 0):
                    print(listNum, i, "x", shopInventory.get(i))
                    listNum += 1
     
            option = input("> ")
            
            if option =="":
                shop()
            elif option in shopInventory and shopInventory.get(i) > 0:
                shopInventory[option] -= 1
                
                if option not in mainPlayer.inventory:
                    mainPlayer.inventory[option] = 1
                else:
                    mainPlayer.inventory[option]+=1
                
            
            option = None
            game_start() 
        else:
            game_start()                
           
def game_start():
    clear_screen()
    option = None
    
    print("What do you want to do?")
    print("[1] Enter Dungeon")
    print("[2] Go to Shop")
    print("[3] Check Stats & Inventory")
    print("[4] Return to Main Menu")
    
    option = input("> ")
    
    if option not in ['1','2', '3', '4', None]:
        option = None
        game_start()
    
    if option == '1':
        enemy_encounter()
    elif option == '4':
        title_screen()
    elif option == '3':
        check_stats()
        check_inv()
        
        print()
        print("Press any button to continue")
        msvcrt.getch()
        
        game_start()
    elif option == '2':
        shop()
        
# Title Screen Function
def title_screen():
    
    clear_screen()
    
    option = None
    
    print("          ==========================")
    print("                   TINKERALL        ")
    print("          ==========================")
    print()
    print("                [1] Play Game")
    print("                [2] Credits")
    print("                [3] Quit")
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

title_screen()
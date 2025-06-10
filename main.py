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
        self.attack = 10
        self.status_effects = []
        self.inventory = {}
        self.gold = 100 
        self.armour = 'None'
        self.weapon = 'None'
mainPlayer = player()

# Declare Master List of Items and Sell Values
pricelist = {
    # Weapons
    "Wooden Sword": 150,
    "Iron Dagger": 100,
    "Rusty Sword": 30,
    "Orc Axe": 200,
    "Cursed Blade": 500,
    
    # Armor / Gear
    "Leather Armor": 150,
    "Bronze Shield": 40,
    
    # Healing Items
    "Potion": 50,
    "Antidote": 50,
    
    # Dropped Items
    "Bone Fragment": 20,
    "Minotaur Horn": 50,
    "Orc Tooth": 50,
    "Dark Crystal": 100,
}

# Make a list of consumables
usable_items = ['Potion', 'Antidote']

# Healing Items List
healing = {
    # HP Recovery
    "Potion": [10, None],
    "Super Potion": [30, None],
    
    # Status Effect Recovery
    "Antidote": [None, "Poison"]
}

# Weapons Item List
weapons = {
    "None": 0,
    "Wooden Sword": 5,
    "Iron Dagger": 7,
    "Rusty Sword": 5,
    "Orc Axe": 10,
    "Cursed Blade": 20,
}

# Armour List
armour = {
    "None": 0,
    "Leather Armor": 10,
    "Bronze Shield": 15,
}

# Declare item effects
def use_item(used):
    
    print("You used", used)
    print()
    
    if healing[used][0] != None:
        mainPlayer.hp += healing[used][0]
        if mainPlayer.hp > mainPlayer.maxhp:
            mainPlayer.hp = mainPlayer.maxhp
        print("Your HP is filled by ", healing[used][0], "!", sep='')
        msvcrt.getch()
    '''
    if used == "Potion":
        mainPlayer.hp += 10
        if mainPlayer.hp > mainPlayer.maxhp:
            mainPlayer.hp = mainPlayer.maxhp
        print("Your HP is filled by 10!")
        msvcrt.getch()
    '''

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

# Check inventory function
def check_inv():
    
    print("Inventory:")
    print()
    
    for i in mainPlayer.inventory:
        if mainPlayer.inventory.get(i) > 0:
            print(i, "x", mainPlayer.inventory.get(i))

# Check stats function
def check_stats():
    print("HP:", mainPlayer.hp)
    print("Attack:", mainPlayer.attack)
    print("Gold:", mainPlayer.gold)

# Item Equip Mechanic
def equip_items():
    
    clear_screen()
    
    option = None
    
    print("Weapon:", mainPlayer.weapon)
    print("Armour:", mainPlayer.armour)
        
    print()
    print("Available Weapons:")    
    
    count = 1
    
    for i in mainPlayer.inventory:
        if i in weapons and mainPlayer.inventory.get(i) > 0:
            print(count,'. ',i,sep='')
            count+=1
    
    print()
    print("Available Armour:")  
    
    count = 1
    
    for i in mainPlayer.inventory:
        if i in armour and mainPlayer.inventory.get(i) > 0:
            print(count,'. ',i,)
            count+=1
    
    print()  
    print("[1] Go Back")
    print()
    print("Please input what you would like to equip.")
    
    option = input("> ")
    
    while option != None and option not in ['1'] and option not in weapons and option not in armour:
        option = input("> ")
        
    if option == '1':
        character_menu()
    elif option in weapons:
        
        mainPlayer.inventory[option]-=1
        
        if mainPlayer.weapon != 'None':
            
            if mainPlayer.weapon not in mainPlayer.inventory:
                mainPlayer.inventory[mainPlayer.weapon] = 1
            else:
                mainPlayer.inventory[mainPlayer.weapon] += 1
        
        mainPlayer.weapon = option
        
    elif option in armour:
        
        mainPlayer.inventory[option]-=1
        
        if mainPlayer.armour != 'None':
            
            if mainPlayer.armour not in mainPlayer.inventory:
                mainPlayer.inventory[mainPlayer.armour] = 1
            else:
                mainPlayer.inventory[mainPlayer.armour] += 1
                
        mainPlayer.armour = option
        
    msvcrt.getch
  
# Check Stats Inv and Equip
def character_menu():
    
    option = None
    
    clear_screen()
    check_stats()
    check_inv()
        
    print("[1] Equip Items")
    print("[2] Go Back")
    
    while option == None and option not in ['1','2']:
        option = input("> ")
    
    if option == '1':
        equip_items()  
  
# Enemy Encounter Function    
def enemy_encounter():
    
    clear_screen()
    
    enemy = random.choice(enemies)()
    action = None
    flee = False
    playerTurn = True
    enemyDefeat = False
    playerDefeat = False
    totalAttack = mainPlayer.attack + weapons.get(mainPlayer.weapon)
    
    print(mainPlayer.weapon, weapons.get(mainPlayer.weapon))
    
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
            print('Enemy HP:', enemy.hp)
            print(totalAttack)
            print()
            print('What would you like to do?')
            print('[1] Attack')
            print('[2] Flee')
            print('[3] Check Stats')
            print("[4] Use Items")
            
            while action not in ['1','2', '3', '4']:
                action = input("> ")
            
            if action == '1':
                
                clear_screen()
                
                enemy.hp -= totalAttack
                print("Player did", totalAttack, "damage to", enemy.name)
                playerTurn = False
                action = '0'
                print()
                print("Press any button to continue")
                msvcrt.getch()
                
            elif action == '2':
                
                clear_screen()
                
                diceRoll = random.randint(0,100) # Remember to reset
                if diceRoll < 75:
                    #print(diceRoll)
                    print('Succesfully fled!')
                    flee = True
                    print()
                    print("Press any button to continue")
                    msvcrt.getch()
                    game_start()
                    #break
                else:
                    print('You were not able to escape')
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
                
                clear_screen()
                
                itemInp = None
                
                check_inv()
                
                print('[1] Go Back')
                print()
                print("Enter the name of the item you want to use")
                
                while itemInp != '1' and (itemInp not in usable_items or itemInp not in mainPlayer.inventory):
                    itemInp = input("> ")
                    print(itemInp)
                
                if itemInp == "1":
                    clear_screen()
                    itemInp = None
                    
                elif itemInp in usable_items and mainPlayer.inventory:
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
            mainPlayer.gold += 10
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
    "Wooden Sword": 1,
    "Leather Armor": 1
}

# Buy Items Mechanic
def buy_items():
    clear_screen()
            
    print("Shopkeeper: Well then let me show you my wares!")
    print()
    print("Gold:", mainPlayer.gold)
    print()
            
    listNum = 1
            
    for i in shopInventory:       
        if shopInventory.get(i) > 0:
            print(listNum,". ", i, " x ", shopInventory.get(i), " - ", pricelist.get(i), " Gold",sep = '')
            listNum += 1
    
    print()
    print("[1] Return") 
    option = input("> ")
            
    if option =="1":
        shop()
    elif option in shopInventory and shopInventory.get(i) > 0:
                
        if mainPlayer.gold > pricelist.get(option):
                    
            mainPlayer.gold -= pricelist.get(option)
                
            shopInventory[option] -= 1
                    
            if option not in mainPlayer.inventory:
                mainPlayer.inventory[option] = 1
            else:
                mainPlayer.inventory[option] += 1
                        
            clear_screen()   
            print("Shopkeeper: Thanks for your business laddie!")
            print()
            print("Obtained 1", option)
                    
            print()
            print("Press any button to continue")
            msvcrt.getch()
                
        else:
            clear_screen()
            print("Shopkeeper: You dont have enough money laddie.")
                    
            print()
            print("Press any button to continue")
            msvcrt.getch()

# Sell Items Mechanic
def sell_items():
    
    clear_screen()
    
    option = None
            
    print("Shopkeeper: What are you selling?")
    
    count = 1
            
    for i in mainPlayer.inventory:
        if mainPlayer.inventory.get(i) > 0:
            print(count, ". ", i, ' x ', mainPlayer.inventory.get(i),' - ',int(pricelist.get(i)/2), sep='')
            count++
    print()
    
    print()
    print("[1] Go Back")
        
    #while option not in mainPlayer.inventory and option != '1':
    option = input("> ")
        
    if option in mainPlayer.inventory and mainPlayer.inventory.get(option) > 0:
        
        clear_screen()
        
        mainPlayer.inventory[option] -= 1
        mainPlayer.gold += int(pricelist.get(option)/2)
        print("Shopkeeper: Thanks for your patronage laddie!")
        print()
        print("You gained", int(pricelist.get(option)/2), "coins!")
        print("You now have", mainPlayer.gold, "coins")
        print()
        print("Press any key to continue.")
        msvcrt.getch()
    else:
        
        clear_screen()
        
        print("Shopkeeper: What are you on about laddie?")
        print()
        print("Press any key to continue.")
        msvcrt.getch()
    shop()

# Shop Mechanics
def shop():
    
    clear_screen()
    
    option = None
    
    print("Shopkeeper: What can I do you for laddie?")
    print()
    print("[1] Buy")
    print("[2] Sell")
    print("[3] Go Back")
    
    while option not in ['1', '2', '3']:
        option = input("> ")
        
        if option == '1':
            
            buy_items()
            
            option = None
            shop()
        elif option == "2":
            
            sell_items()
             
        else:
            game_start()                

# Main Hub           
def game_start():
    clear_screen()
    option = None
    
    print("What do you want to do?")
    print()
    print("[1] Enter Dungeon")
    print("[2] Go to Shop")
    print("[3] Check Stats & Inventory")
    print("[4] Return to Main Menu")
    
    option = input("> ")
    
    while option not in ['1','2', '3', '4'] and option != None:
        option = input("> ")
    
    if option == '1':
        enemy_encounter()
    elif option == '4':
        title_screen()
    elif option == '3':
        clear_screen()
        character_menu()      
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

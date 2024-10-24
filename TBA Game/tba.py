# imports
import random
import time
import sys

#classes
class Room:
     def __init__(self):
        #weeeee
        self.coords = 0,0
        self.rng = random.random()
        self.enemy = 0
        self.chest = 0
        self.stairs = 0
        self.rest = 0
        if self.rng > 0.25:
            self.enemy = 1
        self.rng = random.random()
        if self.rng > 0.5:
            self.chest = 1
        self.rng = random.random()
        if self.rng > 0.9:
            self.stairs = 1
        if self.stairs == 0 and self.enemy == 0 and self.chest == 0:
            self.rest = 1
class Enemy:
    def __init__(self,name,diff):
        self.name = name
        self.hp = 50
        self.atk = 10
        self.defence = 0
        self.difficulty = diff
        for i in range(diff):
            rng = random.randint(0,3)
            if rng == 1:
                self.hp += random.randint(5,10)
            elif rng == 2:
                self.atk += random.randint(1,3)
            else:
                self.defence += 1
    def __repr__(self):
        return "Enemy " + str(self.name) + "\n"+line()+"\nAttack: " + str(self.atk) + "\nHealth: " + str(self.hp) + "\n" + line()
    def printable(self):
        return "Enemy " + str(self.name) + "\n"+line()+"\nAttack: " + str(self.atk) + "\nHealth: " + str(self.hp) + "\n" + line()
    def attack(self):
        dmg =  round(self.atk * (random.random()*2+1),2) - self.defence
        if dmg < 0:
            dmg = 0
        return round(dmg,2)
    def damage(self,dmg):
        self.hp = self.hp - (dmg - self.defence)
class Item:
    def __init__(self,name,slot="Not Equippable",defmod=0,atkmod=0,value=0,special="None"):
        self.name = name
        self.defmod = defmod
        self.atkmod = atkmod
        self.value = value
        self.special = special
        self.slot = slot
    def __repr__(self):
        return "\n" + str(self.name) + " - " + str(self.slot) + "\n" + line() + "\nIncreases defence by " + str(self.defmod) + "\nIncreases attack by " + str(self.atkmod) + "\nValue: " + str(self.value) + "\n" + line()
    def printable(self):
        return "\n" + str(self.name) + " - " + str(self.slot) + "\n" + line() + "\nIncreases defence by " + str(self.defmod) + "\nIncreases attack by " + str(self.atkmod) + "\nValue: " + str(self.value) + "\n" + line()
class Player:
    def __init__(self,name):
        self.name = name
        self.hp = 100
        self.maxhp = 100
        self.attack = 20
        self.defence = 0
        self.level = 1
        self.xp = 0
        self.xpneeded = 100
        self.gear = {
            'Helmet' : Item("Tiny Hat","Helmet"),
            'Armor' : Item("Shirt","Armor"),
            'Leggings' : Item("Pants","Leggings"),
            'Gloves' : Item("Rough Leather Gloves","Gloves"),
            'Boots' : Item("Boots","Boots"),
            'Weapon' : Item("Stick","Weapon")
        }
        self.inventory = []
    def __repr__(self):
        return line() + "\n" + str(self.name) + " - Level " + str(self.level) + " -  XP: " + str(self.xp) + "/" + str(self.xpneeded) + "\n" + line() + "\nHP: " + str(self.hp) + "/" + str(self.maxhp) + "\nAttack: " + str(self.attack) + "\nDefence: " + str(self.defence) + "\n" + line()
    def items(self):
        timeprint(self.gear["Helmet"].printable())
        timeprint(self.gear["Armor"].printable())
        timeprint(self.gear["Leggings"].printable())
        timeprint(self.gear["Gloves"].printable())
        timeprint(self.gear["Boots"].printable())
        timeprint(self.gear["Weapon"].printable())
    def equip(self,item):
        slot = item.slot
        self.defence -= self.gear[slot].defmod
        self.attack -= self.gear[slot].atkmod
        self.attack += item.atkmod
        self.defence += item.defmod
        olditem = self.gear[slot]
        self.gear[slot] = item
        return olditem
    def showinv(self):
        counter = 0
        timeprint("Equipped items:")
        for i in self.gear:
            print(self.gear[i])
            time.sleep(0.5)
        for i in self.inventory:
            counter += 1
            timeprint("Item " + str(counter) + ":")
            print(i)
            time.sleep(0.5)
        equipper = intput("Which item do you want to equip?")
        try:
            olditem = self.equip(self.inventory[equipper - 1])
            self.inventory[equipper-1] = olditem
        except:
            timeprint("That didn't work.")


# globals
global p
p = Player(input("What is your name?"))
global firstbattle
firstbattle = True

# functions
def cs():
    # for clearing screen
    print('\033c')
def timeprint(text):
    # non-instant typing
    punctuation = {
    "." : 0.25,
    "!" : 0.15,
    "?" : 0.15,
    "," : 0.05,
    ":" : 0.1
    }
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char in punctuation:
            time.sleep(punctuation[char])
        else:
            time.sleep(random.random()/20)
    print()
    time.sleep(0.25)
def intput(text):
    #input but requires integer
    while True:
        try:
            timeprint(text)
            ans = input("> ")
            return int(ans)
        except:
            timeprint("That is not a number. Try again.")
def strput(text):
    #input but requires string
    timeprint(text)
    ans = input("> ")
    return str(ans)
def line():
    # l i n e
    return "-----------------------"
def randitem():
    #item generator
    global p
    slots = ["Helmet","Armor","Boots","Leggings","Gloves","Weapon","Weapon"]
    itemslot = slots[random.randint(0,6)]
    points = int(p.level * random.randint(1,5)) + random.randint(1,10)
    itematk = 0
    itemdef = 0
    if itemslot == "Weapon":
        itematk = int(points * (random.random()+0.75))
        itemdef = int(points * (random.random()-0.5))
        if itemdef < 0:
            itemdef = 0
    else:
        itemdef = int(points/2)+1
    itemvalue = int(points * (random.random()+1) * random.randint(1,10) * 2.5)
    itemname = ""
    weapontable = ["Sword","Mace","Axe","Fork","Halberd","Spear","Hammer","Gauntlets","Potato"]
    qualityverbsbad = ["Broken","Old","Moldy","Weak","Worthless"]
    qualityverbsgood = ["Reinforced","Rare","Decorated","Novice","Upgraded"]
    qualityverbsgreat = ["Epic","Royal","Masterwork","Adept","Special"]
    qualityverbsawesome = ["Legendary","Ascendant","Unique","Expert","Masterful"]
    defenceverbs = ["Guarding","Blocking","Shielding","Not-Dying","Bastion","Protecting","Nullifying"]
    attackverbs = ["Slashing","Mauling","Destroying","Bonking","Lancing","Attacking"]
    if points < 15:
        itemname += random.choice(qualityverbsbad) + " "
    elif points < 25:
        itemname += random.choice(qualityverbsgood) + " "
    elif points < 50:
        itemname += random.choice(qualityverbsgreat) + " "
    else:
        itemname += random.choice(qualityverbsawesome) + " "
    if itemdef >= 3:
        itemname += random.choice(defenceverbs) + " "
    else:
        itemdef = 0
    if itemslot != "Weapon":
        itemname += itemslot
    else:
        itemname += random.choice(weapontable)
    if itematk >= 5: 
        itemname += " of " + random.choice(attackverbs)
    item = Item(itemname,itemslot,itemdef,itematk,itemvalue)
    return item
def generateenemy(floor):
    global p
    name = ""
    diff = int((floor + p.level) * (random.random()+1))
    enemy = Enemy("",diff)
    names = ["Bear", "Goblin", "Spiky Wall", "Tax Agent", "Skeleton", "Potato"]
    nameshp = ["Large","Huge","Persistent","Healthy"]
    namesatk = ["Angry","Strong","Mean","Destructive"]
    namesdef = ["Unyielding","Resistant","Immune","Shielded"]
    if enemy.hp > enemy.atk*5 and enemy.hp > enemy.defence*10:
        name += random.choice(nameshp)
        name += " "
        name += random.choice(names)
    if enemy.atk * 5 > enemy.hp and enemy.atk > enemy.defence*2:
        name += random.choice(namesatk)
        name += " "
        name += random.choice(names)
    if enemy.defence * 2 > enemy.atk and enemy.defence * 10 > enemy.hp:
        name += random.choice(namesdef)
        name += " "
        name += random.choice(names)
    else:
        name = random.choice(names)
    enemy.name = name
    return enemy
def generateroom(coords):
    room = Room()
    room.coords = coords
    return room
def battle(enemy):
    cs()
    global p
    global firstbattle
    print(p)
    timeprint("You are entering battle with a " + enemy.name + ".")
    pstunned = False
    estunned = False
    if firstbattle:
        timeprint("Since this is your first battle, I will explain how combat works.")
        print("You and the enemy will take turns fighting.")
        print("On your turn, you may attack high, medium, or low.")
        print("The enemy will guard at random one of these directions.")
        print("If you hit where the enemy is guarding, you will become stunned for one turn.")
        print("If you are stunned, you cannot block, and you deal half damage.")
        print("On the enemy's turn, you also can block and stun the enemy.")
        print("Whoever is reduced to 0 hp first loses.")
        strput("Press enter to continue.")
        firstbattle = False
    while p.hp > 0:
        cs()
        print(p)
        if pstunned:
            timeprint("You are stunned and will deal half damage.")
        timeprint("It is your turn.")
        playerdir = strput("Where will you attack, high, middle, or low?").lower()
        if playerdir not in ["high","middle","low"]:
            timeprint("You fumble with your weapon.")
            timeprint("Input high, middle, or low.")
            playerdir = strput("Where will you attack, high, middle, or low?").lower()
            if playerdir not in ["high","middle","low"]:
                timeprint("You fumble with your weapon again.")
                timeprint("The enemy looks at you confused.")
                timeprint("Embarrased, you swing wildly.")
                playerdir = "middle"
        if estunned:
            enemydir = 'no'
        else:
            enemydir = random.choice(["high","middle","low"])
        damage = int(p.attack * (random.random()+0.5))
        if pstunned:
            damage = damage / 2
            timeprint("Your damage was halved because you were stunned.")
            pstunned = False
        timeprint("You swing " + playerdir + ".")
        if enemydir == "no":
            timeprint("The enemy is stunned and cannot block.")
        else:
            timeprint("The " + enemy.name + " blocked " + enemydir + ".")
        if enemydir == playerdir:
            timeprint("The " + enemy.name + " blocked your attack!")
            pstunned = True
            timeprint("You become stunned, and half of your damage was blocked.")
            damage = damage / 2
        damage = int(damage)
        damage = damage - enemy.defence
        if damage < 0:
            damage = 0
        timeprint("You hit the " + enemy.name + " for " + str(damage) + " damage.")
        enemy.hp = enemy.hp - damage
        time.sleep(0.5)
        cs()
        print(p)
        if enemy.hp > 0:
            timeprint("It is the " + enemy.name + "'s turn. It has " + str(enemy.hp) + " health left.")
            if pstunned:
                playerdir = "no"
            else:
                playerdir = strput("Where would you like to block, high, middle, or low?").lower()
                if playerdir not in ["high","middle","low"]:
                    timeprint("You fumble with your weapon.")
                    timeprint("Input high, middle, or low.")
                    playerdir = strput("Where will you block, high, middle, or low?").lower()
                if playerdir not in ["high","middle","low"]:
                    timeprint("You fumble with your weapon again.")
                    timeprint("The enemy looks at you confused.")
                    timeprint("Embarrased, you block wildly.")
                    playerdir = "middle"
            damage = int(enemy.atk * (random.random()+0.5))
            enemydir = random.choice(["high","middle","low"])
            if estunned:
                damage = damage/2
                estunned = False
                timeprint("The " + enemy.name + " is stunned and will deal half damage.")
            if playerdir != "no":
                timeprint("You blocked " + playerdir + ".")
            timeprint("The enemy attacked " + enemydir + ".")
            if playerdir == enemydir:
                timeprint("You blocked the attack!")
                timeprint("The enemy is stunned, and will deal half damage.")
                estunned = True
                damage = damage/2
            damage = int(damage - p.defence)
            if damage < 0:
                damage = 0
            timeprint("The enemy hit you for " + str(damage) + " damage.")
            p.hp -= damage
            time.sleep(0.5)
        else:
            timeprint("The " + enemy.name + " falls.")
            xp = int(enemy.difficulty * (random.random() + random.random() + 1) * 10)
            timeprint("You gain " + str(xp) + " XP.")
            p.xp += xp
            return "win"
    timeprint("The " + enemy.name + " has defeated you.")
    time.sleep(0.5)
    return "lose"
def score(floor):
    global p
    score = 0
    timeprint("SCORE:")
    print(line())
    timeprint("From levels you gained: " + str(p.level * 1000))
    score += p.level*1000
    timeprint("From leftover XP you got: " + (p.xp) /1000)
    score += p.xp/1000
    timeprint("From floors cleared you got: " + floor*2500)
    score += floor*2500
    timeprint("ITEMS SCORING:")
    print(line())
    for i in p.inventory:
        timeprint(i.name + " gives " + str(i.value))
        score += i.value
    for i in p.gear:
        j = p.gear[i]
        timeprint(j.name + " gives " + str(j.value))
        score += j.value
    strput("Press enter to continue.")
    cs()
    timeprint("TOTAL SCORE:")
    timeprint("-+0+-")
    time.sleep(0.1)
    for i in range(score):
        print("TOTAL SCORE:")
        print("-+" + str(i+1) + "+-")
        time.sleep(random.random()/10)
# variables
cs()
firstroom = Room()
firstroom.coords = 0,0
firstroom.stairs = 0
firstroom.enemy = 0
firstroom.rest = 1
rooms = [firstroom]
coords = 0,0
floor = 1
boss = False
room = None
counter = 0
roompos = None
while True:
    cs()
    print(p)
    counter = 0
    roompos = None
    room = None
    for i in rooms:
        if i.coords == coords:
            room = i
            roompos = counter
        counter += 1
    if not room:
        room = generateroom(coords)
        rooms.append(room)
        roompos = -1
    if boss:
        boss = False
        room.chest = 1
        room.stairs = 1
        room.enemy = 2
        room.rest = 1
    timeprint("You are on floor " + str(floor) + ".")
    timeprint("You are at the room at " + str(coords) + ".")
    while p.xp > p.xpneeded:
        timeprint("You have leveled up!")
        p.xp -= p.xpneeded
        p.level += 1
        p.xpneeded += p.xpneeded * 1.5
        upgraded = False
        timeprint("Choose between one of three upgrades:")
        hpup = random.randint(p.level*2,p.level*5)
        dmgup = random.randint(p.level,p.level*3)
        defup = random.randint(p.level,int(p.level*1.5))
        timeprint("Upgrade 1: Increase HP by " + str(hpup) + " permanently.")
        timeprint("Upgrade 2: Increase attack by " + str(dmgup) + " permanently.")
        timeprint("Upgrade 3: Increase defence by " + str(defup) + " permanently.")
        while upgraded == False:
            choice = intput("Which upgrade would you like?")
            if choice == 1:
                p.maxhp += hpup
                upgraded = True
            elif choice == 2:
                p.attack += dmgup
                upgraded = True
            elif choice == 3:
                p.defence += defup
                upgraded = True
            else:
                timeprint("Try again.")
    if room.enemy == 1:
        timeprint("An enemy is in this room. Starting battle...")
        enemy = generateenemy(floor)
        winlose = battle(enemy)
        if winlose =="win":
            timeprint("You defeat the " + enemy.name + " and move on.")
            room.enemy = 0
        else:
            break
    elif room.enemy == 2:
        enemy = generateenemy(floor * 2)
        timeprint("You are in a huge room, about five times bigger than you're used to.")
        timeprint("Suddenly, a huge monster attacks you from the side!")
        winlose = battle(enemy)
        if winlose =="win":
            timeprint("You defeat the " + enemy.name + " and move on.")
            room.enemy = 0
        else:
            break
    if room.chest == 1:
        timeprint("There is a chest in the corner.")
        yn = strput("Open it? (y/n)")
        if yn == "y":
            item = randitem()
            timeprint("You open the chest, and inside is a " + item.name + "!")
            room.chest = 0
            p.inventory = p.inventory + [item]
        else:
            timeprint("You leave the chest closed.")
    if room.rest == 1:
        timeprint("This room is empty, and is a prime spot to rest and take a break.")
        yn = strput("Rest to recover health?").lower()
        if yn == "y":
            timeprint("You doze off for a bit...")
            timeprint(". . .")
            timeprint("Well, that was nice!")
            heal = int(p.maxhp/2.5)
            if heal > p.maxhp - p.hp:
                heal = p.maxhp - p.hp
            timeprint("You healed " + str(heal) + " HP.")
            p.hp += heal
            if p.hp > p.maxhp:
                p.hp = p.maxhp
            room.rest = 0
        else:
            timeprint("Now isn't the time to rest. You should keep moving.")    
    if room.stairs == 1:
        timeprint("There are a set of stairs in this room.")
        yn = strput("Do you want to go up the stairs? (y/n)")
        if yn == "y":
            timeprint("You descend down the stairs.")
            timeprint("A gate above the stairs is open, and you go through.")
            timeprint("Suddenly, the gate slams shut behind you!")
            if floor == 2:
                timeprint("You think you would have learned from the first gate.")
            elif floor == 3:
                timeprint("... and there it goes again. You know, these gates won't change the more you forget about them.")
            elif floor == 4:
                timeprint("Seriously, how many gates is it going to take to get you to stop?")
            elif floor == 5:
                timeprint("Well, at least enemies can't get up here.")
            elif floor > 5:
                timeprint(". . . again.")
            rooms = [firstroom]
            room = None
            roompos = 0
            floor += 1
            if floor % 2 == 0:
                boss = True
    if room:
        direction = strput("Which way do you want to go? North, East, South, or West? \nAlternatively, you could view your inventory and equip items.").lower()
        if direction == "north":
            coords = coords[0],coords[1]+1
        elif direction == "east":
            coords = coords[0]-1,coords[1]
        elif direction == "south":
            coords = coords[0],coords[1]-1
        elif direction == "west":
            coords = coords[0]+1,coords[1]
        elif direction == "equip" or direction == "inv" or direction == "inventory":
            p.showinv()
        elif direction == "ber":
            cmd = strput("CMD:").lower()
            if cmd == "kill":
                p.hp = 0 
            if cmd == "chest":
                room.chest = 1
            if cmd == "stairs":
                room.stairs = 1
    if room:
        rooms[roompos] = room
    else:
        timeprint("You sit around for a bit.")
    strput("Press enter to continue.")
    
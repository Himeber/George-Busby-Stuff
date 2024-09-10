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
def generateenemy():
    global p
    name = ""
    diff = int(p.level * (random.random()+1))
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
global p
p = Player(input("What is your name?"))
global firstbattle
firstbattle = True
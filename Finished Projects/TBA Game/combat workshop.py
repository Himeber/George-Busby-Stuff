# imports
import random
import time
import sys
# functions
def cs():
    print('\033c')
def timeprint(text):
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
            time.sleep(random.random()/25)
    print()
    time.sleep(0.25)
def intput(text):
    while True:
        try:
            timeprint(text)
            ans = input("> ")
            return int(ans)
        except:
            timeprint("That is not a number. Try again.")
def strput(text):
    timeprint(text)
    ans = input("> ")
    return str(ans)
def line():
    return "-----------------------"
def combat(enemy):
    global player
    turn = "player"
    while player.hp > 0 and enemy.hp > 0:
        if turn == "player":
            if player.stunned:
                timeprint("You are stunned and cannot act.")
                player.stunned = False
                turn = "enemy"
            else:
                timeprint("It is your turn.")
                action = strput("What would you like to do?").lower()
                if action == "attack":
                    damage = round(player.atk * (0.75 + random.random()),1)-enemy.defence
                    timeprint("You hit the enemy for " + str(damage - enemy.defence) + " damage.")
                    enemy.hp = enemy.hp - damage
                    timeprint("The " + enemy.name + " has " + str(enemy.hp) + " hp.")
                elif "cast" in action:
                    action = action[5:]
                    if action in player.skills:
                        ability = player.skills[action]
                        damage,healing,stunned = ability.use(enemy)
                        if damage == "no":
                            timeprint(f"You don't have enough {ability.costtype} to use {ability.name}.")
                        else:
                            timeprint(f"You use {ability.name}.")
                            if damage > 0:
                                timeprint(f"You dealt {str(damage)} damage.")
                            if healing > 0:
                                timeprint(f"You healed for {str(healing)} HP.")
                            if stunned:
                                timeprint("You stunned the enemy.")
                            turn = "enemy"
                    else:
                        timeprint(f"You do not have the ability to use {str(action)}.")
        elif turn == "enemy":
            if enemy.stunned:
                timeprint("The enemy is stunned and cannot act.")
                enemy.stunned = False
                turn = "player"
            else:
                damage = enemy.atk * (random.random() + 0.5)
                damage -= player.defence
class Player:
    def __init__(self):
        self.name = None
        self.hp = 10
        self.atk = 0
        self.defence = 0
        self.energy = 25
        self.maxenergy = 100
        self.mana = 25
        self.maxmana = 100
        self.stunned = False
        self.skills = {

        }
    def __repr__(self):
        thingy = line() + "\n" + self.name + "\n" + line()
        thingy += "\nHP: " + str(self.hp) + "/" + str(self.maxhp)
        thingy += "\nAttack: " + str(atk) + " | Defence: " + str(defence)
class Enemy:
    def __init__(self,name="Bob",hp=10,atk=1,defence=0):
        self.name = name
        self.hp = hp
        self.maxhp = hp
        self.atk = atk
        self.defence = defence
        self.stunned = False
class Spell:
    def __init__(self,name,cost=0,costtype="Energy",damage=0,heal=0,stun=False,crit=False,critchance=0):
        self.name = name
        self.damage = damage
        self.heal = heal
        self.cost = cost
        self.stun = stun
        self.crit = crit
        self.critchance = critchance
        self.costtype = costtype
    def __repr__(self):
        thing = line() + "\n" + self.name + " | Cost: " + str(self.cost) + " " + self.costtype + "\n" + line()
        if self.damage > 0:
            thing += "\nDamage: " + str(self.damage)
        try:
            if self.heal > 0:
                thing += "\nHeals by  " + str(self.heal)
        except:
            pass
        if self.heal == "lifesteal":
            thing += "\nLifesteal"
        if self.stun:
            thing += "\nStuns the enemy"
        if self.crit:
            thing += "\nHas a " + str(self.critchance) + "% chance to crit the enemy"
        thing += "\n" + line()
        return(thing)
    def __str__(self):
        thing = line() + "\n" + self.name + " | Cost: " + str(self.cost) + " " + self.costtype + "\n" + line()
        if self.damage > 0:
            thing += "\nDamage: " + str(self.damage)
        try:
            if self.heal > 0:
                thing += "\nHeals by  " + str(self.heal)
        except:
            pass
        if self.heal == "lifesteal":
            thing += "\nLifesteal"
        if self.stun:
            thing += "\nStuns the enemy"
        if self.crit:
            thing += "\nHas a " + str(self.critchance) + "% chance to crit the enemy"
        thing += "\n" + line()
        return(str(thing))
    def use(self,target):
        global player
        canUse = False
        damage = self.damage * (1+(player.atk/10))
        if self.costtype == 'Energy':
            if player.energy >= self.cost:
                canUse = True
                player.energy -= self.cost
            else:
                pass
        elif self.costtype == 'Mana':
            if player.mana >= self.cost:
                canUse = True
                player.mana -= self.cost
            else:
                pass
        if not canUse:
            return "no","no","no"
        if self.crit:
            rng = random.random()
            if rng < self.critchance/100:
                damage *= 2
        if damage != 0:
            damage -= target.defence
        if damage < 0:
            damage = 0
        healing = self.heal
        if healing == "lifesteal":
            healing = damage
        if self.stun:
            target.stunned=True
        target.hp -= damage
        player.hp += healing
        return int(damage),int(healing),self.stun
global player
player = Player()
cs()
fireball = Spell("Fireball",5,"Mana",10,0,False,True,25)
print(fireball)
heal = Spell("Heal",5,"Mana",0,10)
bonk = Spell("Bonk",5,"Energy",15,0,True,True,5)
player.skills["fireball"] = fireball
player.skills["bonk"] = bonk
player.skills['heal'] = heal
combat(Enemy())
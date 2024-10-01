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
    while player.hp > 0 and enemy.hp > 0:
        pass
class Player:
    def __init__(self):
        self.name = None
        self.hp = 10
        self.atk = 0
        self.defence = 0
        self.energy = 25
        self.mana = 25
    def __repr__(self):
        thingy = line() + "\n" + self.name + "\n" + line()
        thingy += "\nHP: " + str(self.hp) + "/" + str(self.maxhp)
        thingy += "\nAttack: " + str(atk) + " | Defence: " + str(defence)
class Enemy:
    def __init__(self,name,hp,atk,defence):
        self.name = name
        self.hp = hp
        self.maxhp = hp
        self.atk = atk
        self.defence = defence
class Spell:
    def __init__(self,name,cost=0,costtype="Energy",damage=0,defence=0,heal=0,stun=0,crit=0,critchance=0):
        self.name = name
        self.damage = 0
        self.defence = 0
        self.heal = 0
        self.cost = 0
        self.stun = False
        self.crit = False
        self.critchance = 0
    def __repr__(self):
        thing = line() + "\n" + self.name + " | Cost: " + str(self.cost) + " " + self.costtype + "\n" + line()
        if self.damage > 0:
            thing += "\nDamage: " + str(self.damage)
        if self.defence > 0:
            thing += "\nIncreases defence by " + str(self.defence)
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
global player
player = Player()
cs()
fireball = Spell("Fireball")
fireball.damage = 25
fireball.crit = True
fireball.critchance = 25
print(fireball)
block = Spell("Block")
block.defence = 5
heal = Spell("Heal")
heal.heal = 10
bonk = Spell("Bonk")
bonk.stun = True
bonk.damage = 10
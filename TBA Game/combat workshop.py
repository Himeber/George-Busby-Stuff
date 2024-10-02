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
    pstunned = False
    estunned = False
    turn = "player"
    while player.hp > 0 and enemy.hp > 0:
        if turn == "player":
            if pstunned:
                timeprint("You are stunned and cannot act.")
                pstunned = False
                turn = "enemy"
            else:
                timeprint("It is your turn.")
                action = strput("What would you like to do?").lower
                if action == "attack":
                    damage = round(player.atk * (0.75 + random.random()),1)-enemy.defence
                    timeprint("You hit the enemy for " + str(damage - enemy.defence) + " damage.")
                    enemy.hp = enemy.hp - damage
                    timeprint("The " + enemy.name + " has " + str(enemy.hp) + " hp.")
                else:
                    if action in player.skills:
                        ability = player.skills(action)
                        damage = ability.damage * (1+(player.damage/10))
                        try:
                            if ability.heal >= 0:
                                heal = ability.heal
                        except:
                            if ability.heal == "lifesteal":
                                heal = ability.damage
                        if ability.crit:
                            critchance = ability.critchance
                        else:
                            critchance = 0
                        stun = ability.stun
                        cost = ability.cost
                        costtype = ability.costtype
                        if costtype == "Energy":
                            timeprint("You use " + ability.name + ".")
                        elif costtype == "Mana":
                            timeprint("You cast " + ability.name + ".")
                        if damage != 0:
                            damage -= enemy.defence
                            if damage < 0:
                                damage = 0
                            enemy.hp = enemy.hp - damage
                        timeprint("You dealt " + str(damage) + " damage.")
                        timeprint("The " + enemy.name + " has " + str(enemy.hp) + " hp.")
                        if heal > 0:
                            if heal > (player.maxhp - player.hp):
                                heal = player.maxhp - player.hp
                            timeprint("You healed for " + str(heal) + " hp.")
                            player.hp += heal
                    else:
                        timeprint("You do not have that ability.")
        elif turn == "enemy":
            if estunned:
                timeprint("The enemy is stunned and cannot act.")
                estunned = False
                turn = "player"
class Player:
    def __init__(self):
        self.name = None
        self.hp = 10
        self.atk = 0
        self.defence = 0
        self.energy = 25
        self.mana = 25
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
class Spell:
    def __init__(self,name,cost=0,costtype="Energy",damage=0,heal=0,stun=0,crit=0,critchance=0):
        self.name = name
        self.damage = 0
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
heal = Spell("Heal")
heal.heal = 10
bonk = Spell("Bonk")
bonk.stun = True
bonk.damage = 10
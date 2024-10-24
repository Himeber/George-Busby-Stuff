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
    ":" : 0.1,
    "-" : 0.01,
    "\n": 0.25
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
class Player:
    def __init__(self,name,hp,defence,attack,speed,mana,energy,xp,xpneeded,level):
        self.name = name
        self.hp = hp
        self.maxhp = hp
        self.basemaxhp = hp
        self.defence = defence
        self.basedefence = defence
        self.attack = attack
        self.baseattack = attack
        self.mana = mana
        self.maxmana = mana
        self.basemana = mana
        self.energy = energy
        self.maxenergy = energy
        self.baseenergy = energy
        self.xp = xp
        self.xpneeded = xpneeded
        self.level = level
        self.path = None
        self.speed = speed
        self.basespeed = speed
        self.abiities = {
            
        }
        self.spells = {

        }
        self.passives = []
        self.basicattack = Ability("Attack",0,None,1,0,False)
    def __repr__(self):
        return(str(f"""{line()}{line()}
{self.name} - Level {str(self.level)} {self.path} - {str(self.xp)}/{str(self.xpneeded)} XP
{line()}{line()}
HP: {str(self.hp)}/{str(self.maxhp)} | Energy: {str(self.energy)}/{str(self.maxenergy)} | Mana: {str(self.mana)}/{str(self.maxmana)}
Attack: {str(self.attack)} | Defence: {str(self.defence)} | Speed: {str(self.speed)}
{line()}{line()}
"""))

    def abilitiesList(self):
        for i in self.abiities:
            j = self.abiities[i]
            timeprint(j)
            timeprint(line())

    def refreshPassives(self):
        attack = 0
        hp = 0
        defence = 0
        crit = False
        critchance = 0
        for passive in self.passives:
            hp += passive.hp
            attack += passive.attack
            defence += passive.defence
            if passive.crit:
                crit = True
                notcritchance = 1 - critchance
                notcritchance *= passive.critchance
                critchance = 1 - notcritchance
        self.maxhp = self.basemaxhp + hp
        self.attack = self.baseattack + attack
        self.defence = self.basedefence + defence
        self.baseattack.crit = crit
        self.baseattack.critchance = critchance
            
class Enemy:
    def __init__(self,name,hp,attack,defence,skills=None):
        self.name = name
        self.hp = hp
        self.maxhp = hp
        self.attack = attack
        self.defence = defence
        self.skills = skills

    def __repr__(self):
        return str(f"""{line()}
{self.name} - {str(self.hp)}/{str(self.maxhp)} HP
{line()}
""")

class Ability:
    def __init__(self,name,cost,costType,damage,healing,stun,stunturns=1,crit=False,critchance=0):
        self.name = name
        self.cost = cost
        self.costtype = costType
        self.damage = damage
        self.healing = healing
        self.stun = stun
        self.stunturns = stunturns
        self.crit = crit
        self.critchance=critchance
        self.special = None

    def __repr__(self):
        returner = str(f"""{line()}
{self.name} - Costs {str(self.cost)} {self.costtype}
{line()}
""")
    if self.damage > 0:
        returner += f"\nDoes {str(self.damage)}x damage"
    if self.healing == "lifesteal":
        returner += f"\nHas lifesteal"
    elif self.healing > 0:
        returner += f"\nHeals you for {str(self.healing)} HP"
    if self.stun:
        if self.stunturns > 1:
            returner += f"\nStuns enemy for {str(stunturns)} turn"
        else:
            returner += f"\nStuns enemy for 1 turn"
    if self.crit:
        returner += f"Has a {str(self.critchance)}% chance to crit"
    returner += "\n" + line()
    return returner

class Passive:
    def __init__(self,name,atk=0,defence=0,hp=0,mana=0,energy=0,speed=0,crit=False,critchance=0,special=None):
        self.name = name
        self.atk = atk
        self.defence = defence
        self.hp = hp
        self.crit = crit
        self.critchance = critchance
        self.energy = 0
        self.mana = 0
        self.speed = 0
        self.special = special

class Path:
    def __init__(self,name):
        self.name = name
        self.abilitesAtLevels = {
            
        }
        self.passivesAtLevels = {

        }
        self.evolution = None

    def addAbility(self,ability,level):
        self.abilitesAtLevels[level] = ability

    def addPassive(self,passive,level):
        self.passivesAtLevels[level] = passive

cs()
name = strput("What is your name?")
player = Player(name,100,10,10,10,100,100,0,1000,1)
paths = []
squire = Path("Squire")
apprentice = Path("Apprentice")
thief = Path("Thief")
ranger = Path("Ranger")
squire.addAbility(Ability("Power Attack",25,"Energy",1.5,0,False,1,True,10))
apprentice.addAbility(Ability("Mana Blast",25,"Mana",1.5,0,False,0,True,10))
print(str(player))
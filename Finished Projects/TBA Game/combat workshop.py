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
        self.defence = defence
        self.attack = attack
        self.mana = mana
        self.maxmana = mana
        self.energy = energy
        self.maxenergy = energy
        self.xp = xp
        self.xpneeded = xpneeded
        self.level = level
        self.path = None
        self.speed = speed
        self.abiities = {
            
        }
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
        return str(f"""{line()}
{self.name} - Costs {str(self.cost)} {self.costtype}
{line()}
Damage: {str(self.damage)}%
Heals you for {ste(self.healing)} HP
""")
player = Player("bob",100,10,10,10,100,100,0,1000,1)
print(str(player))
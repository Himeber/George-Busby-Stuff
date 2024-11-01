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
    "\n": 0.25
    }
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char in punctuation:
            time.sleep(punctuation[char])
        else:
            time.sleep(random.random()/50)
    print()
    time.sleep(0.05)

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
class Monster:
    def __init__(self,name,hp,atk,defence):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defence = defence
    
    def fight(self,enemy):
        if self.name == enemy.name:
            return f"{self.name} won't fight it's friend."
        else:
            dmg = self.atk - enemy.defence
            if dmg < 0:
                dmg = 0
            enemy.hp -= dmg
            return f"{self.name} dealt {str(dmg)} damage to {enemy.name}."

class Bear(Monster):
    def __init__(self, name="Bear", hp=random.randint(25,50), atk=random.randint(3,15), defence=random.randint(0,3)):
        super().__init__(name, hp, atk, defence)

    def fight(self,enemy):
        if isinstance(enemy,Bear):
            return f"{self.name} won't fight it's friend."
        else:
            dmg = int(self.atk * (random.random() + 0.5)) - enemy.defence
            if dmg < 0:
                dmg = 0
            enemy.hp -= dmg
            return f"{self.name} dealt {str(dmg)} damage to {enemy.name}."
        
class Mup(Monster):
    def __init__(self, name="Mup", hp=random.randint(25,50), atk=random.randint(3,15), defence=random.randint(0,3)):
        super().__init__(name, hp, atk, defence)

    def fight(self,enemy):
        if isinstance(enemy,Mup) or isinstance(enemy,StabbyMup):
            return f"{self.name} won't fight it's friend."
        else:
            dmg = int(self.atk * (random.random() + random.random())) - enemy.defence
            if dmg < 0:
                dmg = 0
            enemy.hp -= dmg
            return f"{self.name} dealt {str(dmg)} damage to {enemy.name}."
        
class StabbyMup(Monster):
    def __init__(self, name="Mup with a knife", hp=random.randint(25,50), atk=random.randint(3,15), defence=random.randint(0,3)):
        super().__init__(name, hp, atk, defence)

    def fight(self,enemy):
        if isinstance(enemy,Mup) or isinstance(enemy,StabbyMup):
            return f"{self.name} won't fight it's friend."
        else:
            dmg = int(self.atk * (random.random() + 0.25))
            if dmg < 0:
                dmg = 0
            enemy.hp -= dmg
            return f"{self.name} dealt {str(dmg)} damage to {enemy.name}."
        
class Potato(Monster):
    def __init__(self, name="A potato", hp=random.randint(25,50), atk=random.randint(3,15), defence=random.randint(0,3)):
        super().__init__(name, hp, atk, defence)

    def fight(self,enemy):
        return f"... Potatoes don't attack..."
    
class Hobo(Monster):
    def __init__(self, name="A hobo", hp=random.randint(25,50), atk=random.randint(3,10), defence=random.randint(0,3)):
        super().__init__(name, hp, atk, defence)

    def fight(self,enemy):
        dmg = int(self.atk * random.random() + enemy.defence/2)
        if dmg < 0:
            dmg = 0
        enemy.hp -= dmg
        return f"{self.name} dealt {str(dmg)} damage to {enemy.name}."

peoples = []
for i in range(0,random.randint(0,5)):
    peoples.append(Bear("Bear " + str(i+1)))
for i in range(0,random.randint(0,5)):
    peoples.append(Mup("Mup " + str(i+1)))
for i in range(0,random.randint(0,5)):
    peoples.append(StabbyMup("Mup with knife " + str(i+1)))
for i in range(0,random.randint(0,5)):
    peoples.append(Hobo("Hobo " + str(i+1)))
fighting = True

while fighting:
    rng = random.randint(0,len(peoples)-1)
    guy1 = peoples[rng]
    rng2 = random.randint(0,len(peoples)-1)
    guy2 = peoples[rng2]
    while rng == rng2:
        rng2 = random.randint(0,len(peoples)-1)
        guy2 = peoples[rng2]
        if len(peoples) <=1:
            break
    timeprint(guy1.fight(guy2))
    timeprint(guy2.fight(guy1))
    if guy1.hp <= 0:
        timeprint(f"{guy1.name} has dieded :(")
        peoples.pop(rng)
        del guy1
    if guy2.hp <= 0:
        timeprint(f"{guy2.name} has dieded :(")
        peoples.pop(rng2)
        del guy2
    mups = False
    bears = False
    hobos = False
    for i in peoples:
        if isinstance(i,Bear):
            bears = True
        elif isinstance(i,Mup) or isinstance(i,StabbyMup):
            mups = True
        elif isinstance(i,Hobo):
            hobos = True
    if mups and (not bears) and (not hobos):
        fighting = False
    elif bears and (not mups) and (not hobos):
        fighting = False
    print(line())
timeprint("The winner(s) are:")
for i in peoples:
    timeprint(i.name)
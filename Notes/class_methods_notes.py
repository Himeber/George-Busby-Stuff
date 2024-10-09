class Pokemon:
    yes = 0
    def __init__(self,name,hp,typ,lvl):
        self.name=name
        self.hp = hp
        self.maxhp = hp
        self.typ = typ
        self.lvl = lvl
    def __str__(self):
        return(f"""----------------
Name: {self.name}
Type: {self.typ}
Level: {self.lvl}
HP: {self.hp} / {self.maxhp}
----------------""")
    def combat(self,other):
        if self.lvl > other.lvl:
            return self.name + " won!"
        elif self.lvl < other.lvl:
            return other.name + " won!"
        else:
            return "lol you tied"
    def levelup(self):
        self.lvl += 1
        self.hp += int(self.hp * 1.1)
    #a class method lol
    #makes it so it can't change instance variables
    @classmethod
    def exist(self):
        self.yes += 1
    #a prebuilt instance that returns Mustard, a level 1 Electric pokemon with 50 hp
    def pikachu():
        return Pokemon("Mustard",50,"Electric",1)
    @staticmethod
    #static methods do not reqiure self or cls
    def hpupdate(poke):
        return poke.hp - 5

eve = Pokemon("DefinitelyAName",392,"Normal",987627465829649739628618348)
print(eve)
oiuhdoiuhs = Pokemon("Pikachu",127,"Electric",42)
print(oiuhdoiuhs)
print(eve.combat(oiuhdoiuhs))

#calling a class method
eve.exist()
mup = Pokemon.pikachu()
print(mup)

#calling a static method
newHp = Pokemon.hpupdate(mup)
mup.hp = newHp
print(mup)
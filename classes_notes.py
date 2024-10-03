#Start classes with the keyword class and name using PascalCase
class Animal:
    #Start with a constructor
    def __init__(self,name,species,age,gender,rarity,likesPlastic=False):
        self.name = name
        self.species = species
        self.age = age
        self.gender = gender
        self.rarity = rarity
        self.likesPlastic = likesPlastic
        self.losses = 0
    #<ethods are functions inside of a class
    def fight(self,other):
        if len(self.name) > len(other.name):
            other.losses += 1
            return True
        elif len(self.name) < len(other.name):
            self.losses += 1
            return False
        else:
            other.losses += 1
            self.losses += 1
            return "tie"
    #Makes a readable string when str() is used or printed
    def __str__(self):
        printer = self.name + " - " + self.gender + " " + self.species + " -  Age " + str(self.age) + "\nRarity - " + self.rarity + " - "
        if self.likesPlastic:
            printer += "Likes eating plastic"
        else:
            printer += "Does not like eating plastic"
        return printer
mup = Animal("Mup","Object of mass destruction",-2,"Nonexistent","no",True)
print(mup)
bear = Animal("Bear","Bear",87621579163497617839465987263729876439,'',"nuclear",True)
print(bear)
print(mup.fight(bear))
mup = None
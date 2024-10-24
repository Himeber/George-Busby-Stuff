#Start classes with the keyword class and name using PascalCase
class Animal:
    #Start with a constructor
    def __init__(self,name="Bob",species="Bob",age=-5,gender="physics",rarity="56",likesPlastic=False):
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
    #Makes a readable string when str() is used or printedededededed
    def __str__(self):
        printer = self.name + " - " + self.gender + " " + self.species + " -  Age " + str(self.age) + "\nRarity - " + self.rarity + " - "
        if self.likesPlastic:
            printer += "Likes eating plastic"
        else:
            printer += "Does not like eating plastic"
        return printer
    def getname(self):
        return self.name
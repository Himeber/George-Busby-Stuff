class PetStore:
    def __init__(self,name,idnumber,animals = []):
        self.name = name
        self.idnumber = idnumber
        self.animals = animals
        self.fatpet = None
    def addpet(self,animal):
        #assert makes sure its an animal and if not ends program
        assert isinstance(animal,Animal)
        self.animals.append(animal)
    def killpet(self,animal):
        try:
            self.animals.remove(animal)
        except:
            print("no worky :(")
        else:
            print("worky :)")
    def overfeed(self,name):
        for pet in self.animals:
            self.fatpet = None
            if pet.name == name:
                self.fatpet = pet
                print("lol you overfed",pet)
                break
        if self.fatpet == None:
            print("you threw 98716497277652 pounds of food on the floor :)")
    def getfat(self):
        return(self.fatpet)
    def forcefeed(self):
        for pet in self.animals:
            petname,yes,fuds = pet.feed()
            print(f"{petname} is eating {fuds} {yes}")
    def getmammals(self):
        return self.get_by_type(Mammal)
    def getreptiles(self):
        return self.get_by_type(Reptile)
    def getdogs(self):
        return self.get_by_type(Dog)
    def getsnakes(self):
        return self.get_by_type(Snake)
    def getturtles(self):
        return self.get_by_type(Turtle)
    def getcats(self):
        return self.get_by_type(Cat)
    def get_by_type(self,typ):
        return [pet for pet in self.animals if isinstance(pet,typ)]
class Animal: 
    def __init__(self,name="Bob"):
        self.name = name
    def __repr__(self):
        return(f"This is {self.name}")
    def feed(self):
        return (self.name, "yummy wee", self.diet)
#dis is how u subclass :)
class Mammal(Animal):
    def __init__(self,name,diet):
        super().__init__(name) # this makes the animal class take care of the name
        self.diet = diet
class Cat(Mammal):
    diet = "mice"
class Dog(Mammal):
    diet = "dog"
class Reptile(Animal):
    diet = "mcdonalds"
#sub-sub classes!
class Snake(Reptile):
    diet = "rodents"
class Turtle(Reptile):
    diet = "livers"
store = PetStore("McDonalds",1997392)
store.addpet(Turtle("Straw"))
store.addpet(Reptile("usadkgfuya"))
print(store.animals)
store.forcefeed()
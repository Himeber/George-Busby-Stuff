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

#ACTUAL CODE STARTS HERE
class DessertItem:
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return str(f"""{self.name}""")

class Candy(DessertItem):
    def __init__(self,name,candyWeight=0.0,pricePerPound=0.0):
        super().__init__(name)
        candyWeight = 0.0
        pricePerPound = 0.0
    def __repr__(self):
        return str(f"""{str(candyWeight)} pound(s) of {self.name}
${str(self.pricePerPound)} per pound""")

class Cookie(DessertItem):
    def __init__(self,name,quantity=0,pricePerDozen=0.0):
        super().__init__(name)
        self.quantity = quantity
        self.pricePerDozen = pricePerDozen
    def __repr__(self):
        return str(f"""{str(self.quantity)} {self.name} cookie(s)
${str(self.pricePerDozen)} per dozen""")

class IceCream(DessertItem):
    def __init__(self,name,scoopCount=0,pricePerScoop=0.0):
        super().__init__(name)
        self.scoopCount = scoopCount
        self.pricePerScoop = pricePerScoop
    def __repr__(self):
        return str(f"""{str(self.scoopCount)} scoop(s) of {self.name} ice cream
${str(self.pricePerScoop)} per scoop""")

class Sundae(IceCream):
    def __init__(self,name,scoopCount=0,pricePerScoop=0.0,toppingName="",toppingPrice=0.0):
        super().__init__(name,scoopCount,pricePerScoop)
        self.toppingName = toppingName
        self.toppingPrice = toppingPrice
    def __repr__(self):
        return str(f"""{str(self.scoopCount)} scoop(s) of {self.name} sundae
${str(self.pricePerScoop)} per scoop
Topped with {self.toppingName}
Topping costs ${str(self.toppingPrice)}""")


desserts = []
fub = DessertItem("Mustard")
chocolateIceCream = IceCream("Chocolate",1,2.49)
bananaSplit = Sundae("Banana Split",1,2.49,"banana",0.49)
chocolateChip = Cookie("Chocolate Chip",1,24.99)
desserts.append(chocolateChip)
desserts.append(bananaSplit)
desserts.append(chocolateIceCream)
desserts.append(fub)
print(line())
for i in desserts:
    timeprint(str(i))
    print(line())
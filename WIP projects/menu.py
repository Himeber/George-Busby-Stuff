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
            time.sleep(random.random()/50)
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
#one method must be new type
class Order:
    def __init__(self,drink=None,appetizer=None,maincourse=None,side1=None,side2=None,dessert=None):
        self.drink = drink
        self.appetizer = appetizer
        self.maincourse = maincourse
        self.side1 = side1
        self.side2 = side2
        self.dessert = dessert
        self.cost = 0
    def __str__(self):
        return f"""{line()}
Order:
{line()}
Drink: {self.drink}
Appetizer: {self.appetizer}
Main Course: {self.maincourse}
Sides: {self.side1} and {self.side2}
Dessert: {self.dessert}
Cost: ${str(self.cost)}
{line()}"""
    def updatecost(self):
        cost = 0
        if self.drink != None:
            cost += self.drink.cost
        if self.appetizer != None:
            cost += self.appetizer.cost
        if self.maincourse != None:
            cost += self.maincourse.cost
        if self.side1 != None:
            cost += self.side1.cost
        if self.side2 != None:
            cost += self.side2.cost
        if self.dessert != None:
            cost += self.dessert.cost
        self.cost = cost
class Fud:
    def __init__(self,name,cost):
        self.name = name
        self.cost = cost
    def __str__(self):
        return f"{self.name} - ${self.cost}"
    @classmethod
    def tenPoundsOfMustard(self):
        return self("Ten Pounds of Mustard",69.99)
    @staticmethod
    def tenPoundsOfMustardize(notMustard):
        mustard = notMustard
        mustard.name = "Ten Pounds of Mustard"
        mustard.cost = 69.99
        return mustard
menu = {
    "Drinks":[Fud.tenPoundsOfMustard()],
    "Appetizers":[Fud.tenPoundsOfMustard()],
    "Main Courses":[Fud.tenPoundsOfMustard()],
    "Sides":[Fud.tenPoundsOfMustard()],
    "Desserts":[Fud.tenPoundsOfMustard()]
}
ordering = True
order = Order()
while ordering:
    cs()
    print("~-Mustard Emporium-~")
    print(line())
    timeprint("Options:")
    timeprint("V: View Order")
    timeprint("M: View Menu")
    timeprint("O: Add an item to your order")
    timeprint("MUSTARD: Turn your order into a lot of mustard")
    timeprint("X: Check out")
    action = strput("What would you like to do?").lower()
    if action == "v":
        timeprint(order)
    elif action == "m":
        for i in menu:
            print(i)
            print(line())
            for j in menu[i]:
                print(j)
    elif action == "o":
        worked = False
        while not worked:
            typ = strput("What kind of food would you like to order?").lower
            if typ in ["side","main course","drink","appetizer","dessert"]:
                worked = True
            else:
                timeprint("You can only order a drink, appetizer, main course, side, or dessert.")
        if typ == 'side':
            worked = False
            while not worked:
                slot = intput("Which side slot do you wont to order, 1 or 2?")
                if slot == 1 or slot == 2:
                    worked = True
                else:
                    timeprint("You can only order two sides.")
            if slot == 1:
                slot == "side1"
            if slot == 2:
                slot = "side2"
        print(menu[typ])
        timeprint("What would you like to order?")
        worked = False
        while not worked:
            number = intput("Type the number of item you want to buy. To cancel, type -1.")
            if number == -1 or menu[typ][number-1]:
                worked = True
            else:
                timeprint("That's not a valid item.")
        if number == -1:
            pass
        else:
            item = menu[typ][number-1]
            if typ == 'side':
                if slot == 1:
                    order.side1 = item
                elif slot == 2:
                    order.side2 = item
            elif typ == "drink":
                order.drink = item
            elif typ == 'main course':
                order.maincourse = item
            elif typ == "appetizer":
                order.appetizer = item
            elif typ == "dessert":
                order.dessert = item
    elif action == "mustard":
        order.drink.tenPoundsOfMustardize()
        order.appetizer.tenPoundsOfMustardize()
        order.maincourse.tenPoundsOfMustardize()
        order.side1.tenPoundsOfMustardize()
        order.side2.tenPoundsOfMustardize()
        order.dessert.tenPoundsOfMustardize()
        timeprint("M U S T A R D\n...\nA P P L I E D")
    strput("Press enter to continue.")
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
class Fud:
    def __init__(self,name=None,cost=None):
        self.name = name
        self.cost = cost
    def __str__(self):
        return f"{self.name} - ${self.cost}"
    @classmethod
    def tenPoundsOfMustard(self):
        return self("Ten Pounds of Mustard",69.99)
    @staticmethod
    def tenPoundsOfMustardize():
        mustard = Fud()
        mustard.name = "Ten Pounds of Mustard"
        mustard.cost = 69.99
        return mustard
class Order:
    def __init__(self,drink=Fud("air",0),appetizer=Fud("air",0),maincourse=Fud("air",0),side1=Fud("air",0),side2=Fud("air",0),dessert=Fud("air",0)):
        self.drink = drink
        self.appetizer = appetizer
        self.maincourse = maincourse
        self.side1 = side1
        self.side2 = side2
        self.dessert = dessert
        self.cost = 0
    def __str__(self):
        return f"""{line()}
Order - ${str(self.cost)}
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
    def calculateTaxes(self):
        	self.cost = self.cost * 1.0775
menu = {
    "Drinks":[Fud.tenPoundsOfMustard(),Fud("Fountain Drink",1.99),Fud("Lemonade",1.50),Fud("Water",0),Fud("Acid",-3475867.00)],
    "Appetizers":[Fud.tenPoundsOfMustard(),Fud("Chips",1.15),Fud("Sliced Fried Potatoes",1.15),Fud("British Crisps",1.15),Fud("Weapons-Grade Uranium",130.78)],
    "Main Courses":[Fud.tenPoundsOfMustard(),Fud("A hot dog",2.50),Fud("BORGOR",5.99),Fud("Steak but someone forgot to put the period in the price",999),Fud("Several pounds of firecrackers",45.00)],
    "Sides":[Fud.tenPoundsOfMustard(),Fud("Refried Beans",3.49),Fud("Nachos",5.25),Fud("Extra mustard",1.49),Fud("Pain",-1997.42)],
    "Desserts":[Fud.tenPoundsOfMustard(),Fud("A Gallon of Ice Cream",6.99),Fud("A Gallon of Iced Crem",0.10),Fud("C O O K I E",2.99),Fud("The store's entire supply of cleaning fluid",-6891762135)]
}
ordering = True
order = Order()
taxesPaid = False
while ordering:
    order.updatecost()
    cs()
    print("\_Mustard Emporium_/")
    print(line())
    timeprint("Options:")
    timeprint("V: View order")
    timeprint("M: View menu")
    timeprint("O: Add an item to your order")
    timeprint("TAXES: Calculate the taxes on your order")
    timeprint("MUSTARD: Turn your order into a lot of mustard")
    timeprint("X: Check out")
    action = strput("What would you like to do?").lower()
    if action == "v":
        timeprint(str(order))
    elif action == "m":
        for i in menu:
            print(line())
            print(i)
            print(line())
            for j in menu[i]:
                print(j)
    elif action == "o":
        worked = False
        while not worked:
            typ = strput("What kind of food would you like to order?").lower()
            typ += "s"
            if typ == "sides" or typ == "main courses" or typ == "drinks" or typ == "appetizers" or typ == "desserts":
                worked = True
                typ = typ.title()
            else:
                timeprint(f"You can't order {typ}!")
                timeprint("You can only order a drink, appetizer, main course, side, or dessert.")
        if typ == 'Sides':
            worked = False
            while not worked:
                slot = intput("Which side slot do you want to order, 1 or 2?")
                if slot == 1 or slot == 2:
                    worked = True
                else:
                    timeprint("You can only order two sides.")
            if slot == 1:
                slot == "side1"
            if slot == 2:
                slot = "side2"
        print(line())
        print(typ)
        counter = 0
        for i in menu[typ.title()]:
            counter += 1
            print(str(counter) + ": " + str(i))
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
            if typ == 'Sides':
                if slot == 1:
                    order.side1 = item
                elif slot == 2:
                    order.side2 = item
            elif typ == "Drinks":
                order.drink = item
            elif typ == 'Main Courses':
                order.maincourse = item
            elif typ == "Appetizers":
                order.appetizer = item
            elif typ == "Desserts":
                order.dessert = item
            taxesPaid = False
    elif action == "mustard":
        order.drink = order.drink.tenPoundsOfMustardize()
        order.appetizer = order.appetizer.tenPoundsOfMustardize()
        order.maincourse = order.maincourse.tenPoundsOfMustardize()
        order.side1 = order.side1.tenPoundsOfMustardize()
        order.side2 = order.side2.tenPoundsOfMustardize()
        order.dessert = order.dessert.tenPoundsOfMustardize()
        timeprint("M U S T A R D\n...\nA P P L I E D")
    elif action == "x":
        timeprint("Checking out...")
        order.updatecost()
        ordering = False
    elif action == "taxes":
        if taxesPaid:
            timeprint("You already calculated your taxes.")
        else:
            timeprint("Calculating taxes...")
            order.updatecost()
            order.calculateTaxes()
            taxesPaid = True
    strput("Press enter to continue.")
cs()
timeprint(f"You had a great time eating {order.appetizer.name} and drinking {order.drink.name} while waiting for your meal to arrive.")
timeprint(f"When your {order.maincourse.name} arrived, you consumed it along with your sides of {order.side1.name} and {order.side2.name}.")
timeprint(f"You then had a delicious dessert of {order.dessert.name}.")
timeprint(f"Afterward, you paid the bill of ${str(order.cost)}.")
timeprint(f"As you were leaving, you had a customary ten pounds of mustard dropped on you. Nice!")
if taxesPaid:
    pass
else:
    timeprint("You then got arrested for not paying sales tax.")
print(line())
timeprint("Your order was:")
timeprint(str(order))
timeprint("Thanks for ordering at the Mustard Emporium!")
mustardIngested = 0
if order.appetizer.name == "Ten Pounds of Mustard":
    mustardIngested += 10
if order.drink.name == "Ten Pounds of Mustard":
    mustardIngested += 10
if order.maincourse.name == "Ten Pounds of Mustard":
    mustardIngested += 10
if order.side1.name == "Ten Pounds of Mustard":
    mustardIngested += 10
if order.side2.name == "Ten Pounds of Mustard":
    mustardIngested += 10
if order.dessert.name == "Ten Pounds of Mustard":
    mustardIngested += 10
if mustardIngested > 0:
    timeprint(f"You ingested {str(mustardIngested)} pounds of mustard.")
    if mustardIngested == 60:
        timeprint("You were rushed to the hospital.")
        timeprint("Turns out eating 50% of your body weight in mustard is fatal.")
        timeprint("you dieded :(")
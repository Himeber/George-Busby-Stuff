class Order:
    def __init__(self,drink=None,appetizer=None,maincourse=None,side1=None,side2=None,dessert=None):
        self.drink = drink
        self.appetizer = appetizer
        self.maincourse = maincourse
        self.side1 = side1
        self.side2 = side2
        self.dessert = dessert
    def __str__(self):
        return "e"
thing = Order("yummy",None,None,"Fuds","Not None")
import math
from abc import ABC, abstractmethod
#polymorphism - to have many forms
#in programming it means something that can do different things depending on what it is given

print(len("hihIIHIHiih")) #len can get lengths of strings
print(len(["hi","i","exist"])) #or lists

class Shape(ABC):
    def __init__(self,x):
        self.x = x

    @abstractmethod
    def area(self):
        return 0

class Square(Shape):
    def area(self):
        return self.x * self.x

class Triangle(Shape):
    def area(self):
        return (self.x * self.x) / 2
    
class Circle(Shape):
    def area(self):
        return self.x * math.pi * self.x

class Rectangle(Shape):
    def __init__(self, x,y):
        super().__init__(x)
        self.y = y
    
    def area(self):
        return self.x * self.y


hed = Circle(10)
body = Square(25)
hat = Triangle(5)

print(hed.area())
print(body.area())
print(hat.area())
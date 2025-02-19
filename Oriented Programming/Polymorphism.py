import random
from abc import abstractmethod


class Shape:

    @abstractmethod  # @abstractmethod oblige les sous classes à comporter la méthode qui suit. ici : aera
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14*self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height*0.5

class Pizza(Circle):
    def __init__(self, topping, radius):
        self.topping = topping
        super().__init__(radius)



x = random.randint(1,20)
y = random.randint(1,20)
shapes = [Circle(x), Square(y), Triangle(x,y), Pizza('Calzone', 5)]

for shape in shapes:
    print(shape.area())


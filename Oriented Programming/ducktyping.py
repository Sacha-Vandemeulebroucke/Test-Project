#"Duck Typing" = Another way to achieve Polymorphism besides Inheritance
#                Object must have the minimum necessary attributes/methods
#                "If it looks like a duck and quacks like a duck, it must be a duck"

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Meow")

class Car:
    alive = False  # Car n'est pas un Animal( il n'hérite pas de cette classe) pourtant il a les mêmes variables de classe et les mêmes méthodes
#                    On peut donc le considérer comme un animal
    def speak(self):
        print("HONK")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)
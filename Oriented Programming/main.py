from tkinter.font import names


class Animal:

    def __init__(self,name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def been_killed(self):
        self.is_alive = False

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    def speak(self):
        print('WOOF')

class Cat(Animal):
    def speak(self):
        print('MIAOUW')

class Mouse(Animal):
    def speak(self):
        print('SQUEEK')



cat1 = Cat("Tik")
animal1 = Animal("George")
animal1.been_killed()
print(animal1.is_alive)
dog1 = Dog("Issou")
dog1.sleep()
dog1.speak()
cat1.speak()

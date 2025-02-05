class Car:

    wheels = 4 #class variable
    number_of_car = 0

    def __init__(self,model,year,mark):
        self.model = model
        self.year = year
        self.mark = mark # instance variable
        Car.number_of_car += 1

car1 = Car("Mustang", 2025, "Ford")
car2 = Car("Mustang", 2025, "Ford")
car3 = Car("Mustang", 2025, "Ford")
car4 = Car("Mustang", 2025, "Ford")
car5 = Car("Mustang", 2025, "Ford")
print(car1.wheels)
print(Car.number_of_car)
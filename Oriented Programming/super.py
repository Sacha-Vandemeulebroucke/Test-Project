
class Shape:
    def __init__(self,color,is_filled):
        self.color = color
        self.is_filled = is_filled

    def display_properties(self):
        print(f"the color is {self.color} and it is {'filled' if self.is_filled else 'not filled'} ")



class Circle(Shape):
    def __init__(self,color,is_filled,radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def area(self):
        super().display_properties()
        print(f"The area is equal to {3.14 * self.radius ** 2}")


class Square(Shape):
    def __init__(self,color,is_filled,width):
        super().__init__(color, is_filled)
        self.width = width

    def area(self):
        super().display_properties()
        print(f"The area is equal to {self.width**2}")


class Triangle(Shape):
    def __init__(self, color, is_filled, width,height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def area(self):
        super().display_properties()
        print(f"The area is equal to {(self.width*self.height)/2}")

circle = Circle("blue",True, 15)
square = Square("red", False, 10)
triangle = Triangle("green", True, 7, 3)
# circle.display_properties()
circle.area()
print(circle.radius)
square.area()
triangle.area()
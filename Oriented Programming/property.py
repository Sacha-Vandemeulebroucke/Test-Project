# @property = Decorator used to define a method as a property (it can be accessed like an attribut)
#             Benefit: Add additional logic when read, write or delete attributes
#             Gives you getter, setter, and deleter method

# https://stackoverflow.com/questions/17330160/how-does-the-property-decorator-work-in-python

class Rectangle:
    def __init__(self, width, height, cote):
        # with the _ between property name like here, it indicates that this is a private variable
        # only for internal use, and we can't access to it directly,we can't do that : rectangle1.width
        self._width = width
        self._height = height
        self.cote = cote

    def show_attributes(self):
        return f"{self._width} - {self._height} - {self.cote}"


# the methods below are getter methods
    @property
    def width(self):
        return f"{self._width:.1f}"

    @property
    def height(self):
        return f"{self._height:.1f}"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than 0")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Width must be greater than 0")

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")

rectangle = Rectangle(3, 4, 8)
print(rectangle.show_attributes())
rectangle.width = 5
rectangle.height = 18
print(rectangle.show_attributes())
print(rectangle.width)
print(rectangle.height)

del rectangle.width
del rectangle.height






# Define a class named Shape and its subclass Square. The Square class has an
# init function which takes length as argument. Both classes have an area function
# which can print the area of the shape where Shape’s area is 0 by default.

class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

shape = Shape()
print(f"Area of shape: {shape.area()}")

sidelen = int(input("Enter the length of side: "))
square = Square(sidelen)
print(f"Area of square: {square.area()}")

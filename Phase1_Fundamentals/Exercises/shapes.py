import math

# Base class
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

# Subclass for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

# Subclass for Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Create objects
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Call area methods
print(f"Area of Circle: {circle.area():.2f}")
print(f"Area of Rectangle: {rectangle.area():.2f}")

print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")

import math

class RegularShape:
    def __init__(self, shape, *params):
        self.shape = shape.lower()
        self.params = params  

    def perimeter(self):
        if self.shape == 'square':
            side = self.params[0]
            return 4 * side
        elif self.shape == 'rectangle':
            length, width = self.params
            return 2 * (length + width)
        elif self.shape == 'circle':
            radius = self.params[0]
            return 2 * math.pi * radius
        else:
            raise ValueError("Unsupported shape for perimeter calculation.")

    def area(self):
        if self.shape == 'square':
            side = self.params[0]
            return side ** 2
        elif self.shape == 'rectangle':
            length, width = self.params
            return length * width
        elif self.shape == 'circle':
            radius = self.params[0]
            return math.pi * radius ** 2
        else:
            raise ValueError("Unsupported shape for area calculation.")

    def display(self):
        try:
            print(f"Perimeter of {self.shape.capitalize()}: {self.perimeter()}")
            print(f"Area of {self.shape.capitalize()}: {self.area()}")
        except ValueError as e:
            print(e)

square = RegularShape('square', 5)

rectangle = RegularShape('rectangle', 8, 4)

circle = RegularShape('circle', 7)

print("Square Calculations:")
square.display()

print("\nRectangle Calculations:")
rectangle.display()

print("\nCircle Calculations:")
circle.display()

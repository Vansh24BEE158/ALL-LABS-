print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")


import math

class Solid:
    def __init__(self, shape, *params):
        self.shape = shape.lower()
        self.params = params

    def surface_area(self):
        if self.shape == 'sphere':
            radius = self.params[0]
            return 4 * math.pi * radius ** 2
        elif self.shape == 'cube':
            side = self.params[0]
            return 6 * side ** 2
        elif self.shape == 'cylinder':
            radius, height = self.params
            return 2 * math.pi * radius * (radius + height)
        else:
            raise ValueError("Unsupported shape for surface area calculation.")

    def volume(self):
        if self.shape == 'sphere':
            radius = self.params[0]
            return (4 / 3) * math.pi * radius ** 3
        elif self.shape == 'cube':
            side = self.params[0]
            return side ** 3
        elif self.shape == 'cylinder':
            radius, height = self.params
            return math.pi * radius ** 2 * height
        else:
            raise ValueError("Unsupported shape for volume calculation.")

    def display(self):
        try:
            print(f"Surface Area of {self.shape.capitalize()}: {self.surface_area()}")
            print(f"Volume of {self.shape.capitalize()}: {self.volume()}")
        except ValueError as e:
            print(e)

sphere = Solid('sphere', 5)

cube = Solid('cube', 4)

cylinder = Solid('cylinder', 3, 7)

print("Sphere Calculations:")
sphere.display()

print("\nCube Calculations:")
cube.display()

print("\nCylinder Calculations:")
cylinder.display()

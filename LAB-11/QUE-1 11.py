print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")


class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    # Addition of two complex numbers
    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    # Subtraction of two complex numbers
    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    # Multiplication of two complex numbers
    def __mul__(self, other):
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imaginary_part = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real_part, imaginary_part)

    # Division of two complex numbers
    def __truediv__(self, other):
        denominator = other.real**2 + other.imaginary**2
        if denominator == 0:
            raise ValueError("Cannot divide by zero.")
        real_part = (self.real * other.real + self.imaginary * other.imaginary) / denominator
        imaginary_part = (self.imaginary * other.real - self.real * other.imaginary) / denominator
        return ComplexNumber(real_part, imaginary_part)

    # Display the complex number in a+bi format
    def __str__(self):
        if self.imaginary < 0:
            return f"{self.real} - {-self.imaginary}i"
        else:
            return f"{self.real} + {self.imaginary}i"


# Test the ComplexNumber class
# Create complex number objects
complex1 = ComplexNumber(3, 4)  # 3 + 4i
complex2 = ComplexNumber(1, 2)  # 1 + 2i

# Perform addition
add_result = complex1 + complex2
print(f"Addition: {add_result}")

# Perform subtraction
sub_result = complex1 - complex2
print(f"Subtraction: {sub_result}")

# Perform multiplication
mul_result = complex1 * complex2
print(f"Multiplication: {mul_result}")

# Perform division
try:
    div_result = complex1 / complex2
    print(f"Division: {div_result}")
except ValueError as e:
    print(e)

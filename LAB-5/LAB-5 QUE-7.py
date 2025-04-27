print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")

import random

# Generate 30 random numbers between -100 and 100
random_numbers = [random.randint(-100, 100) for _ in range(30)]
print("Generated list of 30 random numbers:", random_numbers)

# Create two lists: one for positive numbers and one for negative numbers
positive_numbers = [num for num in random_numbers if num > 0]
negative_numbers = [num for num in random_numbers if num < 0]

# Print the positive and negative numbers lists
print("List of positive numbers:", positive_numbers)
print("List of negative numbers:", negative_numbers)

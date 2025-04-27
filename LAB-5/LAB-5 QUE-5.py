print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")

import random

# Generate 20 random integers and store them in a list
random_integers = [random.randint(1, 100) for _ in range(20)]
print("Generated list of 20 random integers:", random_integers)

# Accept a number from the user
num = int(input("Enter a number to find its positions in the list: "))

# Find and print the positions of all occurrences of the number
positions = [index for index, value in enumerate(random_integers) if value == num]

if positions:
    print(f"The number {num} occurs at positions: {positions}")
else:
    print(f"The number {num} is not found in the list.")

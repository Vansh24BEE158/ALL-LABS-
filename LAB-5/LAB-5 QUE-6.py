print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")

import random

# Generate 50 random numbers in the range 1 to 30
random_numbers = [random.randint(1, 30) for _ in range(50)]
print("List of 50 random numbers:", random_numbers)

# Remove duplicates by converting the list to a set
unique_numbers = list(set(random_numbers))

# Print the list after removing duplicates
print("List after removing duplicates:", unique_numbers)

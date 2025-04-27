print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")

import random

# Generate a list of 5 odd integers
odd_integers = [random.choice(range(1, 100, 2)) for _ in range(5)]
print("List of 5 odd integers:", odd_integers)

# Generate a list of 4 even integers
even_integers = [random.choice(range(2, 100, 2)) for _ in range(4)]
print("List of 4 even integers:", even_integers)

# Replace the third element of odd_integers with the list of even integers
odd_integers[2] = even_integers
print("Odd integers list after replacement of third element:", odd_integers)

# Flatten the list
flattened_list = []
for item in odd_integers:
    if isinstance(item, list):
        flattened_list.extend(item)
    else:
        flattened_list.append(item)

print("Flattened list:", flattened_list)

# Sort the flattened list
flattened_list.sort()
print("Sorted flattened list:", flattened_list)

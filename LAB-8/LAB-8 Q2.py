print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")

import random

random_numbers = set(random.sample(range(15, 46), 10))

print("Original Set:", random_numbers)

count_less_than_30 = sum(1 for num in random_numbers if num < 30)
print("Count of numbers less than 30:", count_less_than_30)

filtered_set = {num for num in random_numbers if num <= 35}
print("Set after deleting numbers greater than 35:", filtered_set)

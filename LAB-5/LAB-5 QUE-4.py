print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")

# Two lists of numbers
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]

# Create a third list containing numbers from list1 that are not in list2
list3 = [num for num in list1 if num not in list2]

# Print the third list
print("Numbers from the first list that are not in the second list:", list3)


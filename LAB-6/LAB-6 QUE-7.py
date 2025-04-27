print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")

original_tuple = (10, 20, 30, 40, 50)

temp_list = list(original_tuple)

del temp_list[2]

modified_tuple = tuple(temp_list)

print("Original tuple:", original_tuple)
print("Modified tuple (after deletion):", modified_tuple)

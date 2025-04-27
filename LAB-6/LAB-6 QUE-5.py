print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")


tuple_list = [("apple", 10), (), ("banana", 20), (), ("cherry", 15), ()]


cleaned_list = [t for t in tuple_list if t != ()]


print("List after removing empty tuples:")
print(cleaned_list)

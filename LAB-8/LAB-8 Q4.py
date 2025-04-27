print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")

names = {"Alice", "Andrew", "Bob", "Brenda", "Angela", "Brian", "Amanda", "Ben"}

names_starting_with_A = set()
names_starting_with_B = set()

for name in names:
    if name.startswith("A"):
        names_starting_with_A.add(name)
    elif name.startswith("B"):
        names_starting_with_B.add(name)

print("Names starting with A:", names_starting_with_A)
print("Names starting with B:", names_starting_with_B)

print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")

names = ["Alice", ("John",), "Sophia", ("David",), "Lily", "Emma", ("Tom",), "Olivia"]

boys = 0
girls = 0

for name in names:
    if isinstance(name, tuple):
        boys += 1
    else:
        girls += 1

print("Number of boys:", boys)
print("Number of girls:", girls)

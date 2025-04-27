print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")


students = [
    (101, "Alice", 18),
    (102, "Bob", 19),
    (103, "Charlie", 17),
    (104, "Diana", 18),
    (105, "Ethan", 20)
]


roll_nos = []
names = []
ages = []


for student in students:
    roll, name, age = student
    roll_nos.append(roll)
    names.append(name)
    ages.append(age)


print("Roll Numbers:", roll_nos)
print("Names:", names)
print("Ages:", ages)

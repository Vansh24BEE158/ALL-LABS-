print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")

names = set()

names.update(["Alice", "Bob", "Charlie", "Diana", "Ethan"])
print("Set after adding 5 names:", names)

if "Charlie" in names:
    names.remove("Charlie")
    names.add("Carlos")
print("Set after modifying 'Charlie' to 'Carlos':", names)

names.discard("Bob")   
names.discard("Diana")
print("Set after deleting 'Bob' and 'Diana':", names)

with open("que3.txt", "r") as f:
    data = f.read()

data_upper = ""
for char in data:
    if char.islower():
        data_upper += char.upper()
    else:
        data_upper += char

with open("que3a.txt", "w") as f:
    f.write(data_upper)

print(data_upper)

    
print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")



user_input=input("enter information for v card \n")
with open("que2.txt",'w') as f:
        f.write(user_input)

with open("que2.txt",'r') as f: 
    data=f.read()
    print(data)

print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")


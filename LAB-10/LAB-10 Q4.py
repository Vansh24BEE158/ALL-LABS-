
with open("que4a.txt", "r") as f1, open("que4b.txt", "r") as f2:
    lines1 = f1.readlines()
    lines2 = f2.readlines()


with open("que4c.txt", "w") as out:
   
    max_len = max(len(lines1), len(lines2))

  
    for i in range(max_len):
        if i < len(lines1):
            out.write(lines1[i])
        if i < len(lines2):
            out.write(lines2[i])

print("Lines merged successfully into 'que4c'")
with open("que4c.txt","r") as f:
    data=f.read()
    print(data)

print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")


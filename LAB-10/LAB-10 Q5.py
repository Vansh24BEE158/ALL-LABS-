
remove_words = ['a', 'an', 'the']


with open("que5.txt", "r") as infile:
    lines = infile.readlines()


with open("que5a.txt", "w") as outfile:
    for line in lines:
        words = line.split()
        
        cleaned_words = [word for word in words if word.lower() not in remove_words]
        
        outfile.write(" ".join(cleaned_words) + "\n")

with open("que5.txt","r") as f:
    data=f.read()
    print(data)
print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")

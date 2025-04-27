print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")

# Input from user
N = int(input("Enter the value of N: "))

# Print N natural numbers in reverse
print(f"First {N} natural numbers in reverse order:")
for i in range(N, 0, -1):
    print(i, end=" ")

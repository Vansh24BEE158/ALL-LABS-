print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")

# Input from user
N = int(input("Enter the number of terms: "))

# Initialize first two terms
a, b = 0, 1

print("Fibonacci Series:")
for _ in range(N):
    print(a, end=" ")
    a, b = b, a + b

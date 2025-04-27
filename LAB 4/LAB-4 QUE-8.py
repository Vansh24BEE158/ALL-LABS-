print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")

# Input from user
num = int(input("Enter a number: "))

# Calculate factorial
factorial = 1
for i in range(1, num + 1):
    factorial *= i

# Print result
print(f"Factorial of {num} is {factorial}")

print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")

import math

# Input values
n = int(input("Enter value of n: "))
r = int(input("Enter value of r: "))

# Calculate nCr and nPr
nCr = math.comb(n, r)  # or use factorial manually: math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
nPr = math.perm(n, r)  # or use: math.factorial(n) // math.factorial(n - r)

# Display results
print(f"nCr ({n}C{r}) = {nCr}")
print(f"nPr ({n}P{r}) = {nPr}")

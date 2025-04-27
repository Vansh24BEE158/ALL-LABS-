print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")

def compute(n):
    """Computes n + nn + nnn + nnnn for a given digit n."""
    n1 = int(str(n))
    n2 = int(str(n) * 2)
    n3 = int(str(n) * 3)
    n4 = int(str(n) * 4)
    return n1 + n2 + n3 + n4

# Testing the function for digits 4 to 7
for i in range(4, 8):
    print(f"compute({i}) = {compute(i)}")

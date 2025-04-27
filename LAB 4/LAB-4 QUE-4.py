print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")

# Pythagorean Triplet: a^2 + b^2 = c^2
print("Pythagorean triplets with side length <= 30:")

for a in range(1, 31):
    for b in range(a, 31):  # Start from 'a' to avoid duplicates
        c_square = a**2 + b**2
        c = int(c_square**0.5)
        if c <= 30 and c**2 == c_square:
            print(f"({a}, {b}, {c})")

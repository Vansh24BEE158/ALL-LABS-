print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_automorphic(n):
    return str(n**2).endswith(str(n))

# Input from user
num = int(input("Enter a number: "))

# Check each property
print(f"Is {num} prime? {'Yes' if is_prime(num) else 'No'}")
print(f"Is {num} perfect? {'Yes' if is_perfect(num) else 'No'}")
print(f"Is {num} Armstrong? {'Yes' if is_armstrong(num) else 'No'}")
print(f"Is {num} palindrome? {'Yes' if is_palindrome(num) else 'No'}")
print(f"Is {num} automorphic? {'Yes' if is_automorphic(num) else 'No'}")

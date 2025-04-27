print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")

def prime_factors(n, factor=2):
    """
    Recursively obtain the prime factors of a given positive integer.
    
    :param n: The number to factorize.
    :param factor: The current factor being checked (default is 2).
    :return: A list of prime factors.
    """
    if n <= 1:
        return []  # Base case: No prime factors for 1 or less

    if n % factor == 0:  
        return [factor] + prime_factors(n // factor, factor)  # Divide and continue with the same factor
    else:
        return prime_factors(n, factor + 1)  # Increment factor if not divisible

# Example usage
num = int(input("Enter a positive integer: "))
print("Prime factors:", prime_factors(num))


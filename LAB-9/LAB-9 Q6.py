print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")


def generate_tuples(n):
    """
    Generate a list of tuples (x, x^2, x^3) for all x from 1 to n (inclusive).
    
    :param n: The upper limit for x.
    :return: A list of tuples.
    """
    return [(x, x**2, x**3) for x in range(1, n+1)]

# Example usage
print(generate_tuples(5))

print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")


def decimal_to_binary(n):
    """
    Recursively find the binary equivalent of a given positive integer.
    
    :param n: The decimal number to convert.
    :return: A string representing the binary equivalent.
    """
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_to_binary(n // 2) + str(n % 2)

# Example usage
num = int(input("Enter a positive integer: "))
print("Binary equivalent:", decimal_to_binary(num))

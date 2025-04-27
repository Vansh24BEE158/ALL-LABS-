print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")


def count_alpha_digits(s):
    """
    Count the number of alphabets and digits in a given string.
    
    :param s: Input string
    :return: Dictionary with counts of alphabets and digits
    """
    result = {"alphabets": 0, "digits": 0}
    
    for char in s:
        if char.isalpha():
            result["alphabets"] += 1
        elif char.isdigit():
            result["digits"] += 1
    
    return result

# Example usage
print(count_alpha_digits("Hello123"))  # Output: {'alphabets': 5, 'digits': 3}
print(count_alpha_digits("2024 is here!"))  # Output: {'alphabets': 6, 'digits': 4}

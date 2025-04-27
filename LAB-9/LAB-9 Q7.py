print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")


def ispalindrome(s):
    """
    Check if a given string is a palindrome, ignoring spaces and case differences.
    
    :param s: Input string
    :return: True if palindrome, False otherwise
    """
    # Remove spaces and convert to lowercase
    cleaned_s = ''.join(s.lower().split())
    
    # Check if the cleaned string is the same when reversed
    return cleaned_s == cleaned_s[::-1]

# Example usage
print(ispalindrome("A man a plan a canal Panama"))  # True
print(ispalindrome("hello"))  # False
print(ispalindrome("Racecar"))  # True

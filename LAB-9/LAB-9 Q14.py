print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")

def count_vowels(s):
    """
    Recursively count the number of vowels in a given string.
    
    :param s: Input string
    :return: Count of vowels in the string
    """
    vowels = "aeiouAEIOU"

    # Base case: If the string is empty, return 0
    if not s:
        return 0

    # Check if the first character is a vowel and recurse on the rest of the string
    return (1 if s[0] in vowels else 0) + count_vowels(s[1:])

# Example usage
string = input("Enter a string: ")
print("Number of vowels:", count_vowels(string))

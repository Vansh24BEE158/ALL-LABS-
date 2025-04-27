print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")

def convert(s):
    """
    Remove duplicate words and return a sorted string.
    
    :param s: Input string containing whitespace-separated words.
    :return: A sorted string with unique words.
    """
    # Split the string into words, convert to a set to remove duplicates
    words = set(s.split())

    # Sort the unique words alphanumerically
    sorted_words = sorted(words)

    # Join the sorted words back into a string
    return ' '.join(sorted_words)

# Example usage
print(convert("banana apple orange apple mango banana"))  
# Output: "apple banana mango orange"

print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")


def frequency(s):
    """
    Compute the frequency of words in a given string and return them in sorted order.
    
    :param s: Input string
    :return: Dictionary with words as keys and their frequencies as values, sorted by words.
    """
    words = s.split()  # Split the string into words
    freq_dict = {}

    # Count word frequencies
    for word in words:
        freq_dict[word] = freq_dict.get(word, 0) + 1

    # Return sorted dictionary
    return dict(sorted(freq_dict.items()))

# Example usage
print(frequency("apple banana apple orange banana apple"))  
# Output: {'apple': 3, 'banana': 2, 'orange': 1}

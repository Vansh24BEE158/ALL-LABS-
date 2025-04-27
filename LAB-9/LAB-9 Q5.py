print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")
import string

def ispangram(sentence):
    # Create a set of all lowercase alphabets
    alphabet_set = set(string.ascii_lowercase)
    
    # Convert the input sentence to lowercase and create a set of characters present in it
    sentence_set = set(sentence.lower())
    
    # Check if the alphabet_set is a subset of sentence_set
    return alphabet_set <= sentence_set

# Test cases
test_sentences = [
    "The quick brown fox jumps over the lazy dog",
    "Crazy Fredrick bought many very exquisite opal jewels",
    "Hello World"
]

for sentence in test_sentences:
    print(f'"{sentence}" is a pangram: {ispangram(sentence)}')

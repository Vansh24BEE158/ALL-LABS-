print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")

input_str = input("Enter a string: ")

char_freq = {}

for char in input_str:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1

    print("Character Frequency:")
for char, freq in char_freq.items():
    print(f"'{char}': {freq}")

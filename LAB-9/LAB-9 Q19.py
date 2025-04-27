print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")

def string_length(s):
    # Base case: empty string
    if s == "":
        return 0
    # Recursive case: count 1 for the first character, then recurse on the rest
    return 1 + string_length(s[1:])

# Example usage
text = "hello world"
length = string_length(text)
print(length)  

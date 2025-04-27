print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")


def count_lower_upper(s):
    count = {"uppercase": 0, "lowercase": 0}
    for char in s:
        if char.isupper():
            count["uppercase"] += 1
        elif char.islower():
            count["lowercase"] += 1
    return count

# Sample string
test_string = "Hello World! Welcome to Python Programming."

# Call the function and print the result
result = count_lower_upper(test_string)
print(result)

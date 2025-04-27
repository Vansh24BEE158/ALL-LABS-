print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")


def sanitize_list(lst):
    # Base case: empty list
    if not lst:
        return []
    
    # Recursive case: process the first element, then recurse on the rest
    head = 0 if lst[0] < 0 else lst[0]
    return [head] + sanitize_list(lst[1:])

# Example usage
numbers = [4, -3, 7, -1, 0, 9, -5]
sanitized = sanitize_list(numbers)
print(sanitized)  

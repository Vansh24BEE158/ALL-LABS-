print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")

def reverse_list(lst):
    # Base case: an empty list or a single-element list is already reversed
    if len(lst) <= 1:
        return lst
    # Recursive case: reverse the rest of the list and append the first element at the end
    return reverse_list(lst[1:]) + [lst[0]]

# Example usage
numbers = [1, 2, 3, 4, 5]
reversed_numbers = reverse_list(numbers)
print(reversed_numbers)  # Output: [5, 4, 3, 2, 1]

print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")


def average_recursive(lst):
    def helper(lst, total=0, count=0):
        # Base case: empty list
        if not lst:
            return total, count
        # Recursive case: add current element to total and increment count
        return helper(lst[1:], total + lst[0], count + 1)

    total, count = helper(lst)
    return total / count if count != 0 else 0

# Example usage
numbers = [10, 20, 30, 40]
avg = average_recursive(numbers)
print(avg)  

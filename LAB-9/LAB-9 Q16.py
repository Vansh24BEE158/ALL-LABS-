print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")

def power(**kwargs):
    a = kwargs.get('a')
    b = kwargs.get('b')

    # Base case: any number to the power of 0 is 1
    if b == 0:
        return 1
    # Recursive case: a^b = a * a^(b-1)
    return a * power(a=a, b=b-1)

# Example usage
result = power(a=2, b=3)
print(result)  

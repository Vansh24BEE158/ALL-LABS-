print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")


def create_array(x, y, z, value):
    """Creates and returns a 3D array of dimensions (x, y, z) initialized to the given value."""
    return [[[value for _ in range(z)] for _ in range(y)] for _ in range(x)]

# Example usage
array = create_array(3, 4, 5, 7)
for layer in array:
    print(layer)

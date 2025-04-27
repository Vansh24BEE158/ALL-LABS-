print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")


def sum_avg(marks):
    """
    Function to calculate the sum and average of marks in five subjects.
    :param marks: List of five numerical values representing marks.
    :return: Tuple containing total sum and average.
    """
    if len(marks) != 5:
        raise ValueError("Please provide exactly five subject marks.")
    
    total = sum(marks)
    average = total / 5
    
    return total, average

# Example usage
marks = [85, 90, 78, 88, 92]  # Example marks
result = sum_avg(marks)
print(f"Total: {result[0]}, Average: {result[1]}")

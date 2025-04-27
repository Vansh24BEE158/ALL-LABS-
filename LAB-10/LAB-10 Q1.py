print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")


import csv

data = [
    ['Name', 'Age', 'Department'],
    ['Alice', 30, 'HR'],
    ['Bob', 25, 'Finance'],
    ['Charlie', 28, 'Engineering'],
    ['Diana', 32, 'Marketing']
]

filename = "employee_data.csv"

with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    writer.writerows(data)

print(f"CSV file '{filename}' created successfully!")

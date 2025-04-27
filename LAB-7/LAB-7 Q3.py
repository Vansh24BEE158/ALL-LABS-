print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")

employees = [
    {"dept_no": 101, "emp_roll": 1, "salary": 50000},
    {"dept_no": 101, "emp_roll": 2, "salary": 60000},
    {"dept_no": 102, "emp_roll": 3, "salary": 45000},
    {"dept_no": 102, "emp_roll": 4, "salary": 70000},
    {"dept_no": 103, "emp_roll": 5, "salary": 40000},
    {"dept_no": 103, "emp_roll": 6, "salary": 55000},
]

dept_salaries = {}

for emp in employees:
    dept = emp["dept_no"]
    salary = emp["salary"]
    dept_salaries.setdefault(dept, []).append(salary)

for dept, salaries in dept_salaries.items():
    print(f"Department {dept}:")
    print(f"  Min Salary: {min(salaries)}")
    print(f"  Max Salary: {max(salaries)}")

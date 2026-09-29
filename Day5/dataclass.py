from dataclasses import dataclass, asdict


@dataclass
class Employee:
    id: int
    name: str
    department: str
    salary: float


employees = [
    Employee(1, "Puneet", "Engineering", 80000),
    Employee(2, "Rahul", "HR", 60000),
    Employee(3, "Aman", "Engineering", 95000),
    Employee(4, "Neha", "Marketing", 70000)
]


# A. Highest-paid employee
def highest_paid(employees):
    return max(employees, key=lambda employee: employee.salary)


# B. Average salary
def average_salary(employees):
    total = sum(employee.salary for employee in employees)
    return total / len(employees)


# C. Employees by department
def get_by_department(employees, department):
    return [
        employee
        for employee in employees
        if employee.department == department
    ]


# D. Give department 10% raise
def give_raise(employees, department):
    for employee in employees:
        if employee.department == department:
            employee.salary *= 1.10


# E. Sort by salary
def sort_by_salary(employees):
    return sorted(
        employees,
        key=lambda employee: employee.salary,
        reverse=True
    )


# F. Convert to dictionaries
def employees_to_dict(employees):
    return [asdict(employee) for employee in employees]


# Testing

print("Highest paid:")
print(highest_paid(employees))

print("\nAverage salary:")
print(average_salary(employees))

print("\nEngineering employees:")
print(get_by_department(employees, "Engineering"))

print("\nGiving Engineering employees 10% raise...")
give_raise(employees, "Engineering")

print("\nAfter raise:")
for employee in employees:
    print(employee)

print("\nSorted by salary:")
for employee in sort_by_salary(employees):
    print(employee)

print("\nAs dictionaries:")
print(employees_to_dict(employees))
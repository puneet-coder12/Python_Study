students = {
    "Rahul": 85,
    "Aman": 72,
    "Priya": 91,
    "Neha": 64,
    "Karan": 78
}

mini = min(students, key = students.get )
maxi = max(students, key = students.get)

sum = 0
for key in students:
    sum+=students[key]
    
avg = sum/len(students)

passed = {}
failed = {}

for [key, values] in students.items():
    if values >= 80:
        passed[key] = values
    elif values < 40:
        failed[key] = values


print(failed)
print(passed)
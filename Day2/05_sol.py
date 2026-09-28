students = [
    {"name": "Aman", "age": 22, "marks": 85},
    {"name": "Rahul", "age": 20, "marks": 92},
    {"name": "Priya", "age": 21, "marks": 78},
    {"name": "Karan", "age": 23, "marks": 92}
]

students.sort(key= lambda x : x.get("marks"), reverse= False)

students.sort(key = lambda x : (-x["marks"], x["name"]))

print(students)
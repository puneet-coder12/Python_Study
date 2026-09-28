def add_student(id, name, marks):
    with open("Day4/student.txt", "a+") as file:
        file.seek(0)
        file.write(f"{id}, {name}, {marks}\n")
        for line in file:
            lis = line.strip().split(", ")

def show_students():
    with open("Day4/student.txt", "a+") as file:
        file.seek(0)
        for line in file:
            lis = line.strip().split(", ")

def search_student(id):
    with open("Day4/student.txt", "a+") as file:
        file.seek(0)
        for line in file:
            lis = line.strip().split(", ")
            if(int(lis[0]) == id):
                print(lis)
                return

def calculate_average():
    with open("Day4/student.txt", "a+") as file:
        file.seek(0)
        sum = 0
        c = 0
        for line in file:
            lis = line.strip().split(", ")
            sum+=int(lis[2])
            ++c
        print(sum/c)
        

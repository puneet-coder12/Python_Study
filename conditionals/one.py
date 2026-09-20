age = input("Tell me your age : ") # take input as a string

age = int(age)

if age < 13:
    print("Child")
elif (age < 20):
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")
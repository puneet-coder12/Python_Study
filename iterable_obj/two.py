
# import os

# print("Working : ",os.listdir())
f = open('iterable_obj/one.py')

print(f.readline())
print(f.readline())
print(f.readline()) # if file reach the end returns an empty string 
print(f.__next__()) # this is what works internally so this will return error when content is finished

for line in open('iterable_obj/one.py'):
    print(line)
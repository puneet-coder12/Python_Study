myList = [1, 2, 3, 4]

I = iter(myList)

print(I) # points to starting pointer or index of list 

print(I.__next__())
print(I.__next__())
print(I.__next__())
print(I.__next__())
print(I.__next__()) # exception because list comes to an end 

# I will always points to starting index or starting pointer of list
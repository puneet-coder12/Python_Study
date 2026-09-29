def countdown(n):
    for val in range(n):
        yield val + 1
        

for val in countdown(5):
    print(val)
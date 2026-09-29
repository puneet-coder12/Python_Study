def myMap(func, iterable):
    result = []
    
    for val in iterable:
        result.append(func(val))
        
    return result

result = myMap(lambda x : x*x, [1, 2, 3, 4, 5])
print(result)
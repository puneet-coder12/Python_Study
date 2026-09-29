def myFilter(func, iterable):
    result = []
    
    for val in iterable:
        if func(val):
            result.append(val)
            
    return result


result = myFilter(lambda x : x%2 == 0, [1, 2, 4, 6])

print(result)
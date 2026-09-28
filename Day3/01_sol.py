def calculation(operation, *args):
    value = 0;
    
    if operation == "add":
        for val in args:
            value+=val
    
    elif operation == "substract":
        for val in args:
            value-=val
    
    elif operation == "multiply":
        value = args[0];
        for val in args:
            value*=val
            
    return value
    
    
print(calculation("multiply", 1, 2, 3, 4, 5))
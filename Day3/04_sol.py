def factorial(n):
    if n <= 1:
        return n
    
    return n *factorial(n-1);

def sum_digits(n):
    sum = 0;
    sum+=n%10
    
    # n = n/10; # gives float value
    n = n//10
    if n == 0:
        return sum
    
    sum+= sum_digits(n);
    return sum 
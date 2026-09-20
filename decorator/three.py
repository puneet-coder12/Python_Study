# Problem: Implement a decorator that caches the return values of a function, so that when it's called with the
# same arguments, the cached value is returned instead of re-executing the function.

def cache(func):
    saved = {}

    def wrapper(*args):
        if args in saved:
            print("Returning cached value")
            return saved[args]

        print("Executing function")
        result = func(*args)
        saved[args] = result

        return result

    return wrapper

@cache
def add(a, b):
    print("Calculating...")
    return a + b


print(add(2, 3))
print(add(2, 3))
print(add(5, 10))
print(add(2, 3))
import time

def timer(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f"Execution time: {end - start}")
        return result
    return wrapper

@timer
def calculate():
    total = 0

    for i in range(1000000):
        total += i

    return total

calculate()
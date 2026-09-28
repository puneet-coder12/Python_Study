numbers = [10, 5, 20, 8, 5, 30, 10, 15]

mini = min(numbers)
maxi = max(numbers)

leng = len(numbers)

i = 0
j = len(numbers) - 1

while i < j:
    numbers[i], numbers[j] = numbers[j], numbers[i]
    i = i+1
    j = j-1
    
sett = set()

for val in numbers:
    sett.add(val)
    
print(f"Unique Values : {sett}")

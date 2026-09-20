car_variety = ["BMW", "Audi", "Mercedes", "Ferrari"]
# print(car_variety)
# print(car_variety[0])

# print(car_variety[1:4]) 
# print(car_variety[-1]) # -ve index from start from 1 not 0

# for car in car_variety:
#     print(car)

# for car in car_variety:
#     print(car, end=" ") # by default end means new line so this will print all in one line with spacing

# car_variety[0] = "Roll Royce"  # works clearly
# print(car_variety)

# car_variety[1:3] = "Rolls Royce" 
#output -> ['BMW', 'R', 'o', 'l', 'l', 's', ' ', 'R', 'o', 'y', 'c', 'e', 'Ferrari']

# what ia does first it remove all the slicing elements and then insert all char particularly as it treats this as an array

#  fix 
# car_variety[1:2] = ["Roll Royce", "Lambo"]
# add new elements from the start of the slicing index and remoce all elements that are coming in slicing


if "BMW" in car_variety:
    print("I have BMW")
    
car_variety.append("Porche")
# car_variety.pop() # remove last element
# car_variety.remove("BMW")

car_variety.insert(1, "Volks") # insert at index 1

# car_variety_copy = car_variety # same reference
car_variety_copy = car_variety.copy() # same value, different referncew

print(car_variety)


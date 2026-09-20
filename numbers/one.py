# s = 'puneet' + 3 # error
# print(s);

print(int(2.3) ) # 2

print(float(2) ) # 2.0

x = 2
y = 3
z = 4
print(x, y, z) # (2, 3, 4) tuple ban jata h lekin print karte time sirf value print hoti h tuple ka reference print nhi hota h

q = x, y, z
print(q) # (2, 3, 4) tuple ban jata h


#study difference between 
repr('puneet') # 'puneet'
str('puneet') # puneet
print('puneet') # puneet

# x < y < z is same as x < y and y < z
# 1 == 2 < 3 is same as 1 == 2 and 2 < 3

import math
print(math.sqrt(16)) # 4.0
print(math.pow(2, 3)) # 8.0
print(math.floor(2.9)) # 2
print(math.floor(-2.9)) # -3
print(math.trunc(2.8)) # 2   run towards 0
print(math.trunc(-2.8)) # -2 run towards 0  
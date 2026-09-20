x = 1
print(x << 1) # left shift by 1

print(x | 1) # bitwise or

import random
print(random.random()) # 0._______
print(random.randint(1, 10)) # random value btw 1 to 10 
print(random.choice([1, 2, 3, 4, 5]))

l1 = [1, 2, 3, 4, 5]
print(random.choice(l1)) 

print(random.shuffle(l1))
print(l1) # shuffle ho gya

print(0.1 + 0.1 + 0.1 - 0.3) #5.551115123125783e-17
# not easy to handle decimal precision so we use library

from decimal import Decimal
Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3') # exprected output
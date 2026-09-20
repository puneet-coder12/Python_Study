name = 'Puneet'
print(name)

slice_n = name[1:3]
print(slice_n) # index 1 to 2 not 3

print(name[:]) # start to end
print(name[-1]) # from last

num_list = "01234567"
print(num_list[0:9:3])  #last parameter means skip value - 1 (values)

print(name.lower())
print(name.upper())
print(name) # no change in real variable bcz of immutable

name.strip() # remove space from front and last

print(name.replace('Pu', 'uu'))
print(name)

print(name.split(', ')) # return list on the basis of ', ' & by default space se split hota h

order = 'I order {} and {}' # {} these are basically placeholder

print(order.format('BMW', 'Audi'))

for letter in name:
    print(letter)
    
print('pun' in name) # is 'pun' present in name variable
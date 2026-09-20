list1 = [1, 2, 3, 4, 5]
list2 = list1;
list1[0] = 10;  # list2[0] = 10 ho jayega

list2 = [1, 2, 3, 4, 5]
list1 = list2;
list1 = [1, 2, 3, 4, 5]
list2[0] = 10; # ab kuch change nhi hoga kyunki list1 aur list2 alag alag reference store kar rhe h

list1 = list2;
# print(list1 == list2) # true aayega kyunki list1 aur list2 ka reference same h
# print(list1 is list2) # true aayega kyunki list1 aur list2 ka reference same h

list2 = [1, 2, 3, 4, 5]
list1 = [1, 2, 3, 4, 5]
print(list1 == list2) # true aayega kyunki list1 aur list2 ka reference alag h but dono ki value same h
print(list1 is list2) # false aayega kyunki list1 aur list2 ka reference alag h

# "is" operator ka use reference check krne k liye hota h
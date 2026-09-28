text = input("Enter a value : ")

freq = {}


for char in text:
    if(freq.get(char) == None):
        freq[char] = 1
    else :
        freq[char] = freq[char] + 1
    
print(freq)
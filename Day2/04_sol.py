text = """
python is easy and python is powerful
python is popular and programming is fun
"""

s = ""

char_freq = {}

# for char in text:
#     if char == " ":
#         if len(s) > 0:
#             char_freq[s] = char_freq.get(s, 0) + 1
#             s = ""
#     else:
#         s = s + char

for word in text.split():
    char_freq[word] = char_freq.get(word, 0) + 1
        
print(char_freq)
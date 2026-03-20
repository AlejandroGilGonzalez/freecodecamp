import re
import random

# Get the dictionary from the txt file:

with open("dics/dics.txt","r",encoding="utf-8") as f:
    dic = f.read()

# Get a random word from the dictionary:

s_word = random.choice(re.findall(r"[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ]+",dic))
print(s_word)

# Print the layout:

layout = r"\w" * len(s_word)
print(layout)

# Find the count of each character to act as probability:

good_chars = "abcdefghijklmnñopqrstuvwxyz"
good_chars += good_chars.upper() + "áéíóúÁÉÍÓÚñÑüÜ"

probab = {}
for char in dic:
    if not char in probab.keys():
        if char in good_chars:
            probab[char] = dic.count(char)

# Sort characters by probability:

top_chars = dict(sorted(probab.items(),key=lambda item:item[1],reverse=True))

# Get a list of all the words with the same length as secret word.

words_list = re.findall(layout,dic)

# Iterate for each word and change the word_list with the specified characters:

new_words = []

for k in top_chars:
    for word in words_list:
        if k in word:
            for match in re.finditer(k,word):
                layout = layout[:match.start()] + k + layout[match.start()+1:]

print(layout)
# Set the layout to change while iterate:








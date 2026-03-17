import re
import random

# Get the dictionary from the txt file:

with open("dics/dics.txt","r",encoding="utf-8") as f:
    dic = f.read()

# Get a random word from the dictionary:

s_word = random.choice(re.findall(r"[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ]+",dic))
print(s_word)

# 
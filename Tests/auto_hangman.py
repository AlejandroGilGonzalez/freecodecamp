import re
from random import randint

# Get the dictionary from the txt file:

with open("dics/dics.txt","r",encoding="utf-8") as f:
    dic = f.read()

# Get a random word from the dictionary:

dic = dic.strip("\n")

print(dic)

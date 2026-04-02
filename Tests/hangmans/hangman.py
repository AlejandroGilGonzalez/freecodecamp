from random import randint as ran
import re

# Open and convert the dictionary file into a dict:

with open("dics/dics.txt","r",encoding="utf-8") as f:
    dict_file = f.read()

values = re.findall(r"^(\w+)",dict_file,re.MULTILINE)

dictionary = {i:k for i,k in enumerate(values)}

# Gets a random number and therefore a random word:

s_word = dictionary[ran(0,len(dictionary))]
print(s_word)

# Prints the s_word layout with a random word in it:

layout ="".join(["_" for i in range(len(s_word)-1)])
r_num = ran(0,len(s_word)-1)
r_char = s_word[r_num]

if s_word.count(r_char) > 1:
    for match in re.finditer(r_char,s_word):
        layout = layout[:match.start()] + r_char + layout[match.start()+1:]
else:
    layout = layout[:r_num] + r_char + layout[r_num:]

print(layout)

# Search for input characters in the s_word and modify the existing layout:
intentos = 10
win = False

while layout != s_word and intentos > 0:
    play = input("Escoja una letra: ")
    if play == "" or len(play)>1:
        print("Escriba solamente 1 letra.")
    if play in s_word:
        for match in re.finditer(play,s_word):
            layout = layout[:match.start()] + play + layout[match.start()+1:]
        print(layout)
    else:
        intentos -= 1
        print(f"Te quedan {intentos} intentos.")
        if intentos == 0:
            print("""\n *** Has perdido *** \n""")
    if layout == s_word:
        win = True
        print("Has ganado.")


    
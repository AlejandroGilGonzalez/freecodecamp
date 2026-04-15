import re
import random
import string

# Get the dictionary from the txt file:
with open("dics/dics.txt","r",encoding="utf-8") as f:
    dic = f.read()

# Get a random word from the dictionary:
#[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ]
s_word = random.choice(re.findall(r"[a-z]+",dic))
print(s_word)

# Set the number of attempts:
attempts = 0

# Set the imposible characters:
imposible_characters = []

# Get a layout for the regex:
layout = "_" * len(s_word)
print(layout)

# Loop for the number of attempts we have: 
while attempts < 10:

    # Print the try number:
    print(f"Intento nº{attempts+1}")

    # Replace underscore per "\w":
    layout = layout.replace("_","\w")

    # Search for the letter that appears the most in the words with that layout:
    posible_words = re.findall(layout, dic, flags= re.IGNORECASE)
    char_appearance = []

    for char in string.ascii_letters:
        if not char in imposible_characters:
            counter = 0
            for word in posible_words:
                if char in word and not char in layout:
                    counter += 1
            char_appearance.append([char,counter])

    char_appearance = sorted(char_appearance, key= lambda x: x[1], reverse= True)

    # Give a name to the most probable character:
    top_char = char_appearance[0][0]
    print(top_char)

    # Replace again layout with underscores "_":
    layout = layout.replace("\w", "_")

    # Compare with secret word to know if the most occurrent character appears or not:
    
    if not top_char in s_word:
        imposible_characters.append(top_char)
        attempts += 1
        print(layout)
        continue
    else:
        imposible_characters.append(top_char)
        attempts += 1
        print(layout)

    # Compare with secret word to know the position of the most occurrent character:
    positions = re.finditer(top_char, s_word)

    # Change the layout with the character we found:
    for match in positions:
        place = match.start()
        layout = layout[:place] + top_char + layout[place + 1:]

    # Print "Winner" if we found the complete word:
    if layout == s_word:
        print("\n*** GANADOR ***")
        print(f"La palabra era: '{layout}'")
        print(f"Numero de intentos: {attempts}")
        break

# Print "Looser" if the program couldn't find the word in the given attempts:
if layout != s_word:
    print("*** PERDEDOR ***")
    print(f"La palabra era: {s_word}")
    print(f"Numero de intentos: {attempts}")
    










# 14/04/2026 Daily Challenge

# Given a string, return the letter from the string that appears last in the alphabet.

# If two or more letters tie for the last in the alphabet, return the first one.

# Ignore all non-letter characters.

import string

def get_last_letter(phrase:str) -> str:

    # Get the entire alphabet:
    alphabet = string.ascii_lowercase

    # Create an index variable to fill with each letter and their index:
    index = []

    # Append each letter index to the index variable:
    for letter in phrase:
        if letter.isalpha():
            letter_index = alphabet.index(letter.lower())
            index.append(letter_index)

    # Get the maximum index:
    max_index = max(index)

    # Get the letters with maximum index in the alphabet:
    
    for letter in phrase:
        if letter.isalpha():
            if alphabet.index(letter.lower()) == max_index:
                return letter

get_last_letter("!#$ er@R asd fT.,> 2t0e9")
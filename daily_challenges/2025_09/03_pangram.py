# 03/09/2025 Daily Challenge

"""
Given a word or sentence and a string of lowercase letters, 
determine if the word or sentence uses all the letters from 
the given set at least once and no other letters.

Ignore non-alphabetical characters in the word or sentence.

Ignore letter casing in the word or sentence.

"""

def is_pangram(sentence:str, letters:str) -> bool:

    # Determine var "letters" as a set of obliged characters:  

    for char in letters:
        if not char in sentence.lower():
            return False
    
    # Determine if all letters are being used:
    
    for char in sentence.lower():
        if char.isalpha():
            if not char in letters:
                return False

    return (True)

is_pangram("Hello World!", "heliowrd")
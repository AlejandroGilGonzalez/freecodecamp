# 09/09/2025 Daily Challenge

# Given a string, determine if all the characters in the string are unique.

# Uppercase and lowercase letters should be considered different characters.

def all_unique(phrase:str) -> bool:

    for char in phrase:
        if phrase.count(char) >= 2:
            return False

    return True

all_unique("QwErTy123!@")
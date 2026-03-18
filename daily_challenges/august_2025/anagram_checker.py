# 16/08/2025

# Given two strings, determine if they are anagrams of each other (contain the same characters in any order).
# Ignore casing and white space.

def are_anagrams(str1:str, str2:str) -> bool:

    # Supres whitespaces and lower the upper characters:

    new_str1 = []
    new_str2 = []

    if " " in str1:
        str1 = str1.replace(" ","")
    if " " in str2:
        str2 = str2.replace(" ","")

    for char in str1.lower():
        new_str1.append(char)
    
    for char in str2.lower():
        new_str2.append(char)

    result = True
    for char in new_str1:
        if not char in new_str2:
            result = False

    return result

are_anagrams("School master", "The classroom")
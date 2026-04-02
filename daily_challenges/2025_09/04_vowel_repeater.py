# 04/09/2025 Daily Challenge

"""
Given a string, return a new version of the string where each vowel 
is duplicated one more time than the previous vowel you encountered.

For instance, the first vowel in the sentence should remain unchanged. 
The second vowel should appear twice in a row. The third vowel should 
appear three times in a row, and so on.


# The letters a, e, i, o, and u, in either uppercase or lowercase, are considered vowels.

# The original vowel should keeps its case.

# Repeated vowels should be lowercase.

# All non-vowel characters should keep their original case.

"""

def repeat_vowels(phrase:str) -> str:

    # Stablish the vowel multiplier that will increase each vowel:

    vowel_mult = 0

    # Create a new string that will have the multiple vowels:

    new_phrase = ""

    # For each vowel in the word multiply it by order of appearance:

    for char in phrase:
        if char.lower() in "aeiou":
            new_phrase += char + (char.lower() * vowel_mult)
            vowel_mult += 1
        else:
            new_phrase += char

    return new_phrase

repeat_vowels("AEIOU")
# 08/09/2025 Daily Challenge

# Given a string containing one or more words, return an acronym of the words using the following constraints:

"""
The acronym should consist of the first letter of each word capitalized, unless otherwise noted.

The acronym should ignore the first letter of these words unless
they are the first word of the given string: a, for, an, and, by, and of.

The acronym letters should be returned in the order they are given.

The acronym should not contain any spaces.

"""

def build_acronym(phrase:str) -> str:

    # List of words we need to ignore if not at first position: 

    may_ingore = ["a","for","and","by","of"]

    # Result string:

    result = ""

    # Split the phrase in words:

    phrase = phrase.split()

    # Capitalize the first letter of each word and return it:

    for i in range(len(phrase)):

        # Ignore the first letter of "a, for, an, and, by, and of" unless they are the first letter of the string:
        
        if phrase[0] in may_ingore:
            result += phrase[0][0].capitalize()
        
        # Capitalize the rest of letters:

        if phrase[i] not in may_ingore:
            result += phrase[i][0].capitalize()

    return (result)

build_acronym("National Aeronautics and Space Administration")
# 26/08/2025 Daily Challenge

# Given a string that contains properly nested parentheses,
# return the decoded version of the string using the following rules:

"""
All characters inside each pair of parentheses should be reversed.

Parentheses should be removed from the final result.

If parentheses are nested, the innermost pair should be reversed first,
and then its result should be included in the reversal of the outer pair.

Assume all parentheses are evenly balanced and correctly nested.

"""

import re

def decode(phrase:str) -> str:

    # Define the number of loops:

    loops = phrase.count("(")

    # With regex we search for the characters inside parenthesis:

    elements_list = []

    for i in range(loops):
        element = re.search(r"(\(\w+\))",phrase) # Searches for inner parenthesis match ()
        element2 = element.group(1).replace("(","")
        element2 = element.group(1).replace(")","")
        phrase = phrase.replace(element2,element2[::-1]) # Substracting the group we don't need anymore
        
    
    print(phrase)

        
decode("(f(b(dc)e)a)")
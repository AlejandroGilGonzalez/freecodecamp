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

    while "(" in phrase:

        # With regex we search for the characters inside parenthesis:

        element = re.search(r"\(([^()]+)\)",phrase)

        # All groups need to be reversed and replaced in the string:

        for i in range(1,len(element.groups()) + 1):
        
            # Reverting the group taken
            
            reversed_element = element.group(i)[::-1]

            # Replacing the reversed element in the given string:

            phrase = phrase.replace(f"({element.group(i)})", reversed_element)
    
    return (phrase)

decode("((is?)(a(t d)h)e(n y( uo)r)aC)")
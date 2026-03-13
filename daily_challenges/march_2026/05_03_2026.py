# 05/03/2026 Daily Challenge

"""
Given a string, return the substring between the two identical characters
that have the smallest number of characters between them (smallest gap)
"""
import re

def smallest_gap(phrase: str) -> str:

    # Gets the repeated characters in the phrase:
    repeated = []

    for char in phrase:
        if phrase.count(char) > 1:
            if not char in repeated: repeated.append(char)
    
    print(repeated)

    # Searches for the gap between each repeated char and appends it to Gaps:
    gaps = []
    for r_char in repeated:
        gap = re.findall(r_char + r"([\w*\{*\^*\**\!*\#*\&*\(*\|*\+*\-*\}*\=*]*)" + r_char,phrase)
        if gap:
            gaps.extend(gap)
    
    print(gaps)

    # Gets the minimum length gap and returns it as a string:

    result = min(gaps, key=len)

    return(result)

smallest_gap("Hello World")
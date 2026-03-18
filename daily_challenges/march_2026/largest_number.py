# 18/03/2026 Daily Challenge

# Given a string of numbers separated by various punctuation, return the largest number.

import re

def largest_number(string:str) -> int:

    # Search for the numbers with a regex:
    result=[]
    numbers = re.findall(r"(-?\d+\.?\d?)",string)
    for num in numbers:
        try:
            result.append(int(num))
        except:
            result.append(float(num))

    return(max(result))

largest_number("12;-50,99.9,49.1!-10.1?88?16")
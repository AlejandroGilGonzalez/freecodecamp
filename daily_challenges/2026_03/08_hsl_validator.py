# 08/03/2026 Daily Challenge

#Given a string, determine whether it is a valid CSS hsl() color value.

"""A valid HSL value must be in the format "hsl(h, s%, l%)", where:

h (hue) must be a number between 0 and 360 (inclusive).
s (saturation) must be a percentage between 0% and 100%.
l (lightness) must be a percentage between 0% and 100%.
Spaces are only allowed:

After the opening parenthesis
Before and/or after the commas
Before and/or after closing parenthesis
Optionally, the value can end with a semi-colon (";").

For example, "hsl(240, 50%, 50%)" is a valid HSL value. """

import re

def is_valid_hsl(hsl:str) -> str:
    # Checks if hsl format given is whether valid or invalid.

    
    lista = re.search(r"hsl\(\s*(\d+)\s*,\s*(\d+)%\s*,\s*(\d+)%\s*\)\s*;?",hsl)
    if lista == None:
        return False
    if lista:
        h,s,l = lista.groups()
    count = 0
    test = False

    if int(h) >= 0 and int(h) <= 360:
        count +=1
    if int(s) >= 0 and int(s) <= 100:
        count+=1
    if int(l) >= 0 and int(l) <= 100:
        count+=1
    if count == 3:
        test = True

    return(test)

is_valid_hsl("hsl (80, 20%, 10%)")
# 02/09/2025 Daily Challenge

# Given a CSS rgb(r, g, b) color string, return its hexadecimal equivalent.
#
# Make any letters lowercase.
#
# Return a # followed by six characters. Don't use any shorthand values.

import re

def rgb_to_hex(rgb:str) -> str:
    
    # Convert the string to a list of numbers:

    rgb_list = re.findall(r"(\d+)", rgb)
    rgb = rgb_list

    for i in range(len(rgb)):
        rgb[i] = int(rgb[i])

    return (f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}")

rgb_to_hex("rgb(255, 255, 255)")
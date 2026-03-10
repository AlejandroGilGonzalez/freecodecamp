# Daily Challenge 06/03/2026

# Given a window size, the width of an element in viewport width "vw" units.
# and the height of an element in viewport height "vh" units, determine the size of the element in pixels.


import re

def get_element_size(window_size: str, element_vw:str, element_vh:str)->str:
    
    # Gets the window size as int and takes the vw and vh percentage of it.

    numbers = list(map(int, re.findall(r"\d+",window_size)))
    element_vw = int(element_vw.replace("vw",""))
    element_vh = int(element_vh.replace("vh",""))
    one = int(numbers[0] * (element_vw/100))
    two = int(numbers[1] * (element_vh/100))
    window_size = str(one) + " x " + str(two)

    return(window_size)


get_element_size("1200 x 800", "50vw", "50vh")
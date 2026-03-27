# 27/03/2026 Daily Challenge

# Given a string, return a new string that is truncated so that the total width of the characters does not exceed 50 units.

"""

Each character has a specific width:

Letters	Width
"ilI"	1
"fjrt"	2
"abcdeghkmnopqrstuvwxyzJL"	3
"ABCDEFGHKMNOPQRSTUVWXYZ"	4

The table above includes all upper and lower case letters. Additionally:

Spaces (" ") have a width of 2

Periods (".") have a width of 1

If the given string is 50 units or less, return the string as-is, otherwise

Truncate the string and add three periods at the end ("...") so it's total width,
including the three periods, is as close as possible to 60 units without going over.

"""

def truncate_text(phrase:str) -> str:

    # Stablish the total permited witdh and the starting width as 0:
    
    total_width = 50
    start_width = 0

    # Search for the different width parameters:

    new_string = ""

    for char in phrase:
        if char in "ilI" or (char in "."):
            #if start_width + 1 < 50:
            start_width += 1
            new_string += char

        elif char in "fjrt" or (char in " "):
            # if start_width + 2 < 50:
            start_width += 2
            new_string += char

        elif char in "abcdeghkmnopqrstuvwxyzJL":
            #if start_width + 3 < 50:
            start_width += 3
            new_string += char

        elif char in "ABCDEFGHKMNOPQRSTUVWXYZ":
            # if start_width + 4 < 50:
            start_width += 4
            new_string += char

        
    print (start_width)
    print (new_string)

truncate_text("The silky smooth sloth")
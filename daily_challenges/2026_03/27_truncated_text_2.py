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

    # Stablish the starting width as 0 and each width in format list:
    
    start_width = 0

    one = list("ilI" + ".")
    two = list("fjrt" + " ")
    three = list("abcdeghkmnopqrstuvwxyzJL")
    four = list("ABCDEFGHKMNOPQRSTUVWXYZ")

    # Sum the different width parameters and creates a new string:

    new_string = ""

    for char in phrase:
        
        # When characters should sum 1:

        if char in one:
            if start_width + 1 <= 50:
                start_width += 1
                new_string += char
            else:
                break

        # When characters should sum 2:

        elif char in two:
            if start_width + 2 <= 50:
                start_width += 2
                new_string += char
            else:
                break

        # When characters should sum 3:

        elif char in three:
            if start_width + 3 <= 50:
                start_width += 3
                new_string += char
            else:
                break

        # When characters should sum 4:

        elif char in four:
            if start_width + 4 <= 50:
                start_width += 4
                new_string += char
            else:
                break

    # Determines if the string should return equal or modified:

    print(new_string)

    if new_string == phrase: # When the string is equal returns the same.
        return new_string
    else:
        if start_width + 3 <= 50: # When the new string can have three dots.
            new_string = new_string + "..."
        else: # When we need to remove the last character:                 
            new_string = new_string[:-1] + "..."

    
    print(start_width)
    return(new_string)

truncate_text("THE LOUD BRIGHT BIRD")
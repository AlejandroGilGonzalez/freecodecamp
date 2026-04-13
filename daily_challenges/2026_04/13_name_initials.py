# 13/04/2026 Daily Challenge

# Given a full name as a string, return their initials.

"""
Names to initialize are separated by a space.
Initials should be made uppercase.
Initials should be separated by dots.

"""

def get_initials(name:str) -> str:

    # Split the name into a list capitalized:
    name = name.split()

    # Give the format to the text:
    new_name = ""

    for word in name:
        new_name += word[0].capitalize() + "."
        
    return new_name

get_initials("Dorothy Vera Clump Haverstock Norris")
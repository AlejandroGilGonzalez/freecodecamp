# 14/08/2025 Daily Challenge

# Given a string, remove all spaces from the string, insert two spaces between every character,
# convert all alphabetical letters to uppercase, and return the result.

# Non-alphabetical characters should remain unchanged (except for spaces).

def space_jam(phrase:str) -> str:

    # Remove all white spaces:

    phrase = phrase.replace(" ", "")
    phrase = phrase.upper()

    # Insert two white spaces between every character:
    new = ""
    for char in phrase:
        new += char + "  "
    
    new = new[:-2]
    
    print(new)
space_jam("free Code Camp")
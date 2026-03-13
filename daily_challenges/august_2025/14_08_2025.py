# 14/08/2025 Daily Challenge

# Given a string, remove all spaces from the string, insert two spaces between every character,
# convert all alphabetical letters to uppercase, and return the result.

# Non-alphabetical characters should remain unchanged (except for spaces).

def space_jam(phrase:str) -> str:

    # Remove all white spaces:

    new = phrase.replace(" ", "")
    print(new)
    # Insert two white spaces between every character:


space_jam("free Code Camp")
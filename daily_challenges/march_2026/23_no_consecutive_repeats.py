# 23/03/2026 Daily Challenge

# Given a string, determine if it has no repeating characters.

# A string has no repeats if it does not have the same character two or more times in a row.

def has_no_repeats(string:str) -> bool:

    # Determine if there is more than 1 word:
    if " " in string:
    # Get each word of the string:
        frase = string.split()
            # Count each character in the word:
        for word in frase:
            for char in word:
                c_count = word.count(char)
            # If there is one repeated return False:
                if c_count >= 2:
                    return False
    else:
        for char in string:
            c_count = string.count(char)
            # If there is one repeated return False:
            if c_count >= 2:
                return False

    return True

has_no_repeats("hello world")
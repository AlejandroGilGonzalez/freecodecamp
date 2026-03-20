# 11/03/2026 Daily Challenge

# Given a string of words, return a new string where each word is replaced by its length.

# Words in the given string will be separated by a single space
# Keep the spaces in the returned string.

def convert_words(words:str) -> str:
    # Gets the length of each word in a string and returns a string showing those lengths

    separated = words.split()

    for i in range(len(separated)):
        separated[i] = str(len(separated[i]))

    result = " ".join(separated)
    
    return (result)

convert_words("Lorem ipsum dolor sit amet consectetur adipiscing elit donec ut ligula vehicula iaculis orci vel semper nisl")
# 21/04/2026 Daily Challenge

# Given a string of words, return only the words with an odd number of letters.

# Words in the given string will be separated by a single space.
# Return the words separated by a single space.

def get_odd_words(phrase:str) -> str:

    # Stablish a list for appending words with odd number of letters:
    odd_words = []

    # Split the string into pieces:
    split_phrase = phrase.split()

    # Loop over all words in the string and count their words:
    for word in split_phrase:
        if len(word) % 2 != 0:
            odd_words.append(word)
    
    # Return odd words joined as a string:
    return (" ".join(odd_words))



get_odd_words("This is a super good test")
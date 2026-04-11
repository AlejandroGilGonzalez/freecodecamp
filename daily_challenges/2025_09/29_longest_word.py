# 29/09/2025 Daily Challenge

# Given a sentence, return the longest word in the sentence.

# Ignore periods (.) when determining word length.
#
# If multiple words are ties for the longest, return the first one that occurs.

import re

def get_longest_word(sentence:str) -> str:

    # Search only words:

    words = re.findall(r"(\w+)", sentence)

    # Zip the length to each word:

    words = list(zip(words, [len(word) for word in words]))

    # Sort words by length and/or index:

    words = sorted(words, key= lambda x: (-x[1], sentence.index(x[0])))

    # Return the longest / longest first occurrence:

    return words[0][0]
   

get_longest_word("This sentence has multiple long words.")
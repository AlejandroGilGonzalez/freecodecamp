# 14/09/2025 Daily Challenge

# Given a paragraph, return an array of the three most frequently occurring words.

"""
- Words in the paragraph will be separated by spaces.
- Ignore case in the given paragraph. For example, treat Hello and hello as the same word.
- Ignore punctuation in the given paragraph. Punctuation consists of commas (,), periods (.), and exclamation points (!).
- The returned array should have all lowercase words.
- The returned array should be in descending order with the most frequently occurring word first.

"""

import re

def get_words(paragraph:str) -> list:

    # Convert all words to lowercase:

    paragraph = paragraph.lower()

    # Get only words from the paragraph:

    words = re.findall(r"(\w+)", paragraph)

    word_set = set(words)

    # Get the words by frequence ocurrence:

    frequence = []

    for word in word_set:
        frequence.append([word, words.count(word)])
        
    # Sort words by appearance:

    frequence = sorted(frequence, key= lambda x: (-x[1], words.index(x[0])))
  
    # Return the repeated words in descending order by how many times they appear:

    result = []

    for i in range(3):
        result.append(frequence[i][0])

    return (result)

get_words("I like coding. I like testing. I love debugging!")
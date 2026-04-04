# 11/09/2025 Daily Challenge

"""
Given a string of words, return a new string with the words in reverse order. 
For example, the first word should be at the end of the returned string,
and the last word should be at the beginning of the returned string.

"""

# In the given string, words can be separated by one or more spaces.
# The returned string should only have one space between words.

def reverse_sentence(sentence:str) -> str:

    # Split the sentence into a list:

    sentence = sentence.split()

    # Join with a space the reversed list:

    result = " ".join(sentence[::-1])
    
    return result

reverse_sentence("npm  install   apt    sudo")
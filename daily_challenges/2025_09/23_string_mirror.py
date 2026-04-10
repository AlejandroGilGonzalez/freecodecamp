# 23/09/2025 Daily Challenge

# Given two strings, determine if the second string is a mirror of the first.

"""
- A string is considered a mirror if it contains the same letters in reverse order.
- Treat uppercase and lowercase letters as distinct.
- Ignore all non-alphabetical characters.

"""
import re

def is_mirror(str1:str, str2:str) -> bool:

    # Search for words only in the first string:

    words_str1 = re.findall(r"(\w+)", str1)
    words_str1 = "".join(words_str1)

    # Search for words only in the second string:

    words_str2 = re.findall(r"(\w+)", str2)
    words_str2 = "".join(words_str2)

    # Check if the first string reversed is the same as string 2:

    if words_str1[::-1] == words_str2:
        return True
    else:
        return False



is_mirror("Hello World", "dlroW-olleH")
# 16/09/2025 Daily Challenge

# Given a paragraph, return a new paragraph where the first letter of each sentence is capitalized.

# All other characters should be preserved.
# Sentences can end with a period (.), one or more question marks (?), or one or more exclamation points (!).

import re

def capitalize(paragraph:str) -> str:

    phrases = re.findall(r"(\w+)", paragraph)

    print(phrases)

    for phrase in phrases:
        paragraph = paragraph.replace(phrase, phrase.capitalize())

    print(paragraph)

    return paragraph

capitalize("hello world. how are you?")
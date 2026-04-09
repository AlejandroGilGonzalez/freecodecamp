# 16/09/2025 Daily Challenge

# Given a paragraph, return a new paragraph where the first letter of each sentence is capitalized.

# All other characters should be preserved.
# Sentences can end with a period (.), one or more question marks (?), or one or more exclamation points (!).

import re

def capitalize(paragraph:str) -> str:

    # Finds the phrases until they end with . ? or !:

    phrases = re.findall(r"([^.?!]+)", paragraph)

    print(phrases)

    # Searches for the first word in each phrase:

    for phrase in phrases:
        first = re.search(r"\s?(\w+)", phrase)
        first = str(first.group(1))

        # Replaces first word with the same but capitalized:

        paragraph = paragraph.replace(first, first.capitalize())

    print (paragraph)
    return paragraph

import re

def capitalize(paragraph:str) -> str:

    # Finds the phrases until they end with . ? or !:

    phrases = re.findall(r"([^.?!]+)", paragraph)

    # Searches for the first word in each phrase:

    for phrase in phrases:

        # If the first character is a white space it capitalizes the word:

        if phrase[0] == " ":
            cap_phrase = " "+(phrase[1:].capitalize())
            paragraph = paragraph.replace(phrase,cap_phrase)

        # Replaces first word with the same but capitalized:

        paragraph = paragraph.replace(phrase, phrase.capitalize())

    return paragraph

capitalize("i did today's coding challenge... it was fun!!")
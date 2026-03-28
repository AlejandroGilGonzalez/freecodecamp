# 25/08/2025 Daily Challenge

# Given a string, return its camel case version using the following rules:

"""
Words in the string argument are separated by one or more characters from the following set: 
space ( ), dash (-), or underscore (_). Treat any sequence of these as a word break.

The first word should be all lowercase.

Each subsequent word should start with an uppercase letter, with the rest of it lowercase.

All spaces and separators should be removed.

"""

def to_camel_case(phrase:str) -> str:

    # Replace the word breakers:

    text = phrase.replace("-"," ")
    text = text.replace("_"," ")

    # Split the string into a list:

    camelcase = text.split()

    # Lowercase the first word: 
    
    camelcase[0] = camelcase[0].lower()

    print(camelcase)

    # Capitalize the following words:

    for i in range(1,len(camelcase[1:])+1):
        camelcase[i] = camelcase[i].capitalize()
    
    # Unite the words in one string with Join:

    result = "".join(camelcase)
    
    return (result)

to_camel_case("secret agent-X")
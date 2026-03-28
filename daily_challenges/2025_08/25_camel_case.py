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

    text = phrase.replace("-","")
    text = text.replace("_","")

    # Split the string into a list:

    camelcase = text.split()

    # Create a new list with the CamelCase 
    
    for word in split_text:
        if word == split_text[0]:
            word = word.upper()
            camelcase.append(word)                           

        camel = word[0].upper() + word[1:]
        camelcase.append(camel)        
    print(camelcase)

    return ""

to_camel_case("hello world")
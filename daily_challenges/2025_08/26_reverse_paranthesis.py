# 26/08/2025 Daily Challenge

# Given a string that contains properly nested parentheses,
# return the decoded version of the string using the following rules:

"""
All characters inside each pair of parentheses should be reversed.

Parentheses should be removed from the final result.

If parentheses are nested, the innermost pair should be reversed first,
and then its result should be included in the reversal of the outer pair.

Assume all parentheses are evenly balanced and correctly nested.

"""

def decode(phrase:str) -> str:

    # Gets the index of every parenthesis:

    parenthesis = []

    for i, char in enumerate(phrase):
        if char in "()":
            parenthesis.append(i)        
    
    print (parenthesis)

    
    # Gets the parenthesis correlation:

    first = 0
    last = -1
    correlation = []

    for i in range(len(parenthesis)//2):
        new = [parenthesis[first],parenthesis[last]]
        correlation.append(new)
        first +=1
        last -=1

    print(correlation)

    # Gets the words in between the parenthesis:

    new_phrase = ""

    for i in range
    
decode("(f(b(dc)e)a)")
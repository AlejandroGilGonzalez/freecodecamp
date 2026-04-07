# 07/04/2026 Daily Challenge

# Given a string, determine if it's a palindrome and return the middle character (if it's odd length) or middle two characters (if it's even).

# A palindrome is a string that is the same forward and backward.
# If it's not a palindrome, return "none".

def palindrome_locator(word:str) -> str:

    upside = word[::-1]

    if upside == word:
        if len(word) % 2 != 0:
            return (word[len(word)//2])
        else:
            one = int((len(word)/2) -1)
            two = int((len(word)/2) + 1)
            return (word[one:two])

    else:
        return ("none")
            

    return ""

palindrome_locator("noon")
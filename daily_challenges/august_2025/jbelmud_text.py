# 15/08/2025 Daily Challenge

# Given a string, return a jumbled version of that string where each word is transformed using the following constraints:
"""
- The first and last letters of the words remain in place
- All letters between the first and last letter are sorted alphabetically.
- The input strings will contain no punctuation, and will be entirely lowercase.
"""

def jbelmu(text:str) -> str:

    text = text.split(" ")
    

    new_text = []
    
    for word in text:
        if len(word) > 1:
            sorted_w = sorted(word[1:-1])
            word = word[0] + "".join(sorted_w) + word[-1]
            new_text.append(word)
        else:
            new_text.append(word)

    return (" ".join(new_text))

jbelmu("i love jumbled text")
# 11/08/2025 Daily Challenge

# Given a string, determine whether the number of vowels 
# in the first half of the string is equal to the number of vowels in the second half.

def is_balanced(phrase:str) -> bool:
    
    # Split the string in 2 halves:

    length = len(phrase)
    if length % 2 != 0:
        first = phrase[:length//2]
        second = phrase[(length//2)+1:]
    else:
        first = phrase[:length//2]
        second = phrase[(length//2):]
    f_count=0
    s_count=0
    for char in first:
        if char.lower() in "aeiou":
            f_count += 1
    for char in second:
        if char.lower() in "aeiou":
            s_count += 1
    
    if f_count == s_count:
        return True
    else:
        return False

is_balanced("racecar")
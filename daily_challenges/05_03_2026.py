# 05/03/2026 Daily Challenge

"""
Given a string, return the substring between the two identical characters
that have the smallest number of characters between them (smallest gap)
"""

def smallest_gap(input: str) -> str:
    gap_chars = {}

    # Counts the repeated characters and their index
    for i in range(len(input)):
        char = input[i]
        if input[i:].count(char) > 1: gap_chars.setdefault(i,char)
    print(gap_chars) 
    
    # Finds the gaps between the repeated characters

    gaps = []
    min_len = len(input)

    for pos, gap_char in gap_chars.items():
        l_find = input.find(gap_char, pos)
        r_find = input.find(gap_char, pos+1)    
        gap = input[l_find+1:r_find]
        gaps.append(gap)
        if len(gap) < min_len: min_len = len(gap)

    for gap in gaps:
        if len(gap) == min_len:
            return( gap )
    return ""

smallest_gap("ABCDAC")
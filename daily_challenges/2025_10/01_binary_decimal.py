# 01/10/2025 Daily Challenge

# Given a string representing a binary number, return its decimal equivalent as a number.

def to_decimal(binary:str) -> int:

    return int(binary, 2)

to_decimal("101")
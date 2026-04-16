# 16/04/2026 Daily Challenge

# Given a string with numbers and other characters, perform math on
# the numbers based on the count of non-digit characters between the numbers.

"""
If the count of characters separating two numbers is even, use addition.
If it's odd, use subtraction.
Consecutive digits form a single number.
Operations are applied left to right.
Ignore leading and trailing characters that aren't digits.

"""
import re

def do_math(math:str) -> int:

    # Search for the numbers in the string:
    numbers = re.findall(r"(\d+)", math)
    
    # For each number and the consecutive one check their index:
    index_number = re.finditer(r"(\d+)",math)
    indexes = []

    for match in index_number:
        indexes.append([match.start(), match.end()])

    # Count the characters between the numbers:
    characters_between = []
    for i in range(len(indexes)-1):
        characters_between.append(abs(indexes[i][1] - indexes[i+1][0]))

    # Do the math:
    result = 0

    # For each range between numbers:
    for i in range(len(characters_between)):
        # When the range is even use addition:
        if characters_between[i] % 2 == 0:
            result = int(numbers[i]) + int(numbers[i+1])
            numbers[i+1] = result
        # When the range is odd use substraction:
        elif characters_between[i] % 2 != 0:
            result = int(numbers[i]) - int(numbers[i+1]) 
            numbers[i+1] = result

    return result

do_math("a.67,1$lk6ldf34@#LD@]2d32d2'2l3,@l3L#@2gh35s09if=df#$t9sm49t0df3$^%[vc;:0:4mt")
# 07/09/2025 Daily Challenge

# Given a string representing a Roman numeral, return its integer value.
#
# Roman numerals consist of the following symbols and values:

"""
Symbol	Value
I	    1
V	    5
X	    10
L	    50
C	    100
D	    500
M	    1000

Numerals are read left to right. If a smaller numeral appears before a larger one, 
the value is subtracted. Otherwise, values are added.

"""

def parse_roman_numeral(numeral:str) -> int:

    # Define the roman numerals value:

    roman_numbers = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }

    # Create a variable for the result:

    result = 0

    # Create a skip list for numerals already used:

    skip = []

    # Loop over each numeral to check if we can add it or substract from the next one:    
    
    for i in range(len(numeral)):
        if i not in skip:
            try:
                if roman_numbers[numeral[i]] >= roman_numbers[numeral[i+1]]:
                    result += roman_numbers[numeral[i]]
                else:
                    result += roman_numbers[numeral[i+1]] - roman_numbers[numeral[i]]
                    skip.append(i+1)
            except:
                result += roman_numbers[numeral[i]]

    return (result)

parse_roman_numeral("CDLX")
# 09/04/2026 Daily Challenge

# Given a bingo number, return the next bingo number sequentially.

# A bingo number is a single letter followed by a number in its range according to this chart:

"""
Letter 	Number Range
"B" 	1-15
"I" 	16-30
"N" 	31-45
"G" 	46-60
"O" 	61-75

"""

def get_next_bingo_number(bingo:str) -> str:

    # Define the maximum bingo values range:

    bingo_values = {
        "B":[1,15],
        "I":[16,30],
        "N":[31,45],
        "G":[46,60],
        "O":[61,75]
    }

    # Split the input into letter and number:

    letter = bingo[0]
    number = int(bingo[1:])

    # Compare the number with the ranges:

    for key, value in bingo_values.items():
        if number + 1 in range(value[0],value[1]+1):
            return (str(key) + str(number+1))
        if number + 1 > 75:
            return "B1"

get_next_bingo_number("I30") 
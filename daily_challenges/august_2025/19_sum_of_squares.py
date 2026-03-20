# 19/08/2025 Daily Challenge

# Given a positive integer up to 1,000, return the sum of all the integers squared from 1 up to the number.

def sum_of_squares(number:int) -> int:

    # Get the square of all the numbers in the given range and sum them together.

    sumas = []

    for i in range(1,number+1):
        sumas.append(i**2)

    return(sum(sumas))

sum_of_squares(5)
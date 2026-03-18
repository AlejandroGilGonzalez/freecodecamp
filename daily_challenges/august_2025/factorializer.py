# 18/08/2025 Daily Challenge

"""
Given an integer from zero to 20, return the factorial of that number.
The factorial of a number is the product of all the numbers between 1 and the given number.
"""

def factorial(number:int) -> int:

    # Multiply all numbers in range of the given number:

    result = 1

    for i in range(number):
        result *= i+1

    return (result)

factorial(5)
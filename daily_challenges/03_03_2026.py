# 03/03/2026 Daily Challenge

# Given two integers, determine how many perfect cubes exist in the range between and including the two numbers.

""" The lower number is not garanteed to be the first argument.
A number is a perfect cube if there exists an integer (n)
where n * n * n = number. For example, 27 is a perfect cube because 3 * 3 * 3 = 27."""

#Challenge:

def count_perfect_cubes(num1:int, num2:int) -> int:
    """returns the perfect cubes in range
        :param num1: minimum
        :param num2: maximum
        :return: perfect cubes count"""

    count = 0
    if num1 < num2:
        minim = num1
        maxim = num2
    else:
        minim = num2
        maxim = num1
    
    if minim > 1: minim = 2

    for num in range(minim, maxim+1):
        num = num ** 3
        if num >= minim and num <= maxim:
            count += 1

    return count
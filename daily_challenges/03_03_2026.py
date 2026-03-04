#03/03/2026 Daily Challenge

# Given two integers, determine how many perfect cubes exist in the range between and including the two numbers.

""" The lower number is not garanteed to be the first argument.
A number is a perfect cube if there exists an integer (n)
where n * n * n = number. For example, 27 is a perfect cube because 3 * 3 * 3 = 27."""

#Challenge:

def count_perfect_cubes(num1, num2):
    """returns the perfect cubes in range
        :param num1: minimum
        :param num2: maximum
        :return: perfect cubes count"""

    count = 0
    if num1 < num2:
        min = num1
        max = num2
    else:
        min = num2
        max = num1
    
    if min > 1:
        for num in range(1, max+1):
            num = num ** 3
            if num >= min and num < max:
                count += 1
    else:
        for num in range(min, max+1):
            num = num ** 3
            if num >= min and num <= max:
                count += 1

    return count
# 25/09/2025 Daily Challenge

# Given an array, return the second largest distinct number.

def second_largest(numbers:list) -> int:

    result = sorted(set(numbers))[-2]

    return result

second_largest([1, 0, -1, 0, 1, 0, -1, 1, 0])
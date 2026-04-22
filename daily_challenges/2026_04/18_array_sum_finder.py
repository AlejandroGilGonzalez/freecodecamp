# 18/04/2026 Daily Challenge

# Given an array of numbers and a target number, return the first subset of two or more numbers that adds up to the target.

"""
The "first" subset is the one whose elements have the lowest possible indices, prioritizing the earliest index first.
Each number in the array may only be used once.
If no valid subset exists, return "Sum not found".

Return the matching numbers as an array in the order they appear in the original array.

"""

def find_sum(arr:list, target:int) -> list:
    
    # Create a list of numbers to return:
    result = []

    # Create a check var:
    check = 0

    # Check which numbers sum to the target:
    for i in range(len(arr)):
        # If adding the number is lower than the target, append it:
        if arr[i] + check < target:
            result.append(arr[i])
            check += arr[i]
        # If adding the number is greater than the target, continue:
        elif arr[i] + check > target:
            continue
        # If adding the number ads up to the target, return the array:
        elif arr[i] + check == target:
            result.append(arr[i])
            print(result)

    return "Sum not found"

find_sum([1, 3, 5, 7], 6)
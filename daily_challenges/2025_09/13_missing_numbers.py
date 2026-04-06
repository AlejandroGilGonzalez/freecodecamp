# 13/09/2025 Daily Challenge

# Given an array of integers from 1 to n, inclusive, return an array of all
# the missing integers between 1 and n (where n is the largest number in the given array).

# The given array may be unsorted and may contain duplicates.
#
# The returned array should be in ascending order.
#
# If no integers are missing, return an empty array.

def find_missing_numbers(arr:list) -> list:

    # Sort the array and get rid of duplicates:

    arr = sorted(set(arr))

    # Create a list for returning the missing numbers:

    missing = []

    # Search for the missing numbers in the sorted array:

    for i in range(1,arr[-1]):
        if not i in arr:
            missing.append(i)

    return missing

find_missing_numbers([1, 2, 3, 4, 5, 7, 8, 9, 10, 12, 6, 8, 9, 3, 2, 10, 7, 4])


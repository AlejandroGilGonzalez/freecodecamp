# 30/08/2025 Daily Challenge

# Given an array of integers, return an array of integers that appear more than once
# in the initial array, sorted in ascending order. If no values appear more than once, return an empty array.
#
# Only include one instance of each value in the returned array.

def find_duplicates(numbers:list) -> list:

    # Create a new array for duplicate numbers:
    
    new_array = []

    # Find the duplicate numbers in the array:

    for number in numbers:
        if numbers.count(number) >= 2:
            if not number in new_array:
                new_array.append(number)

    # Return a set of the duplicate numbers in ascending order:
    
    return(sorted(new_array))


find_duplicates([2, 34, 0, 1, -6, 23, 5, 3, 2, 5, 67, -6, 23, 2, 43, 2, 12, 0, 2, 4, 4])
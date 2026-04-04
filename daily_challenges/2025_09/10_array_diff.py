# 10/09/2025 Daily Challenge

# Given two arrays with strings values, return a new array containing all the values that appear in only one of the arrays.

# The returned array should be sorted in alphabetical order.

def array_diff(arr1:list, arr2:list) -> list:

    # Convert both arrays into sets and check with difference opperators for the different ones:

    result = set(arr1) ^ set(arr2)

    # Return the result in alphabetical order:

    return sorted(list(result))

array_diff(["one", "two", "three", "four", "six"], ["one", "three", "eight"])
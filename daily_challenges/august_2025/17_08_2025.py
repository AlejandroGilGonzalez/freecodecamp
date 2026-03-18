# 17/08/2025 Daily Challenge

"""
Given an array of numbers and an integer target,
find two unique numbers in the array that add up to the target value.
Return an array with the indices of those two numbers,
or "Target not found" if no two numbers sum up to the target.

The returned array should have the indices in ascending order.
"""

def find_target(numbers:list, target:int) -> list or str:

    # Get the two unique numbers that add up to the target:

    for i in range(len(numbers)):        
        for j in range(i+1,len(numbers)):
            if numbers[i]+numbers[j] == target:
                result = [i,j]
                return(result)
    
    return "Target not found"



find_target([3, 2, 4, 5], 6)
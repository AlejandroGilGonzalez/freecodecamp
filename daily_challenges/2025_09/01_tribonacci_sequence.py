# 01/09/2025 Daily Challenge

# The Tribonacci sequence is a series of numbers where each number is the sum of the three preceding ones.
#  
# When starting with 0, 0 and 1, the first 10 numbers in the sequence are 0, 0, 1, 1, 2, 4, 7, 13, 24, 44.

"""
Given an array containing the first three numbers of a Tribonacci sequence, 
and an integer representing the length of the sequence, return an array containing the sequence of the given length.

Your function should handle sequences of any length greater than or equal to zero.
If the length is zero, return an empty array.
Note that the starting numbers are part of the sequence.

"""

def tribonacci_sequence(start_sequence:list, length:int) -> list:

    # Sum the 3 preceding numbers for creating a new one:

    for i in range(length):
        new = start_sequence[i] + start_sequence[i+1] + start_sequence[i+2] 
        start_sequence.append(new) # Appending the new number to the sequence

    # We need to return a new array for the given length:

    new_array = []

    # Create a loop to get only the given length numbers:

    for i in range(length):
        new_array.append(start_sequence[i])


    return new_array

tribonacci_sequence([0, 0, 1], 0)
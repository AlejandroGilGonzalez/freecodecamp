# 13/08/2025 Daily Challenge

# Given an array containing the first two numbers of a Fibonacci sequence,
# and an integer representing the length of the sequence, return an array containing the sequence of the given length.

def fibonacci_sequence(start_sequence:list, length:int) -> list:

    new_sequence = []
    for i in range(length):
        new = start_sequence[i] + start_sequence[i+1]
        start_sequence.append(new)

    for i in range(length):
        new_sequence.append(start_sequence[i]) 

    return (new_sequence)

fibonacci_sequence([0, 1], 0)
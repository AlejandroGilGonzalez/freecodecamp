# 16/03/2026 Daily Challenge

# Given two integers, determine if you can evenly divide the first one by the second one.

def is_evenly_divisible(a, b):

    if a % b == 0:
        return True
    else:
        return False

is_evenly_divisible(4, 2)
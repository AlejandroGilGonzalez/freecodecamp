# 01/03/2026 Daily Challenge

# Given an array, determine if it is flat

# An array is flat if none of its elements are arrays.

def is_flat(arr):
    flat = True
    for i in arr:
        if isinstance(i,list):
            flat = False
            break
        else:
            flat = True
    return flat

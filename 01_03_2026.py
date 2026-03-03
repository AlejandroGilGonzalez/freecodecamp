# 01/03/2026 Daily Challenge

# Given an array, determine if it is flat

def is_flat(arr):
    flat = True
    for i in arr:
        if isinstance(i,(list,tuple,set)):
            flat = False
            break
        else:
            flat = True
    return flat

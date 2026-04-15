# 15/04/2026 Daily Challenge

# Given an array of integers, return a new array using the following rules:

# Sort the integers in ascending order
# Then swap all values whose index is a multiple of 3 with the value before it.

def sort_and_swap(array:list) -> list:

    # Sort the index in ascending order:
    array_c = array.copy()
    array_c = sorted(array_c)

    print(array_c)
    
    # Swap all values with index multiple of 3 by the value before it:
    for i in range(len(array_c)):
        if not i == 0:
            if i % 3 == 0:
                next_num = array_c[i-1]
                prev_num = array_c[i]
                array_c[i-1] = prev_num
                array_c[i] = next_num

    return array_c

sort_and_swap([9, 7, 5, 3, 1, 2, 4, 6, 8])
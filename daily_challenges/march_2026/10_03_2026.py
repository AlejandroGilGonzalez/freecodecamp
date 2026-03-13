# 10/03/2026 Daily Challenge

# Given an array, a value to insert into the array, and an index to insert the value at,
# return a new array with the value inserted at the specified index.

def insert_into_array(arr:list, value:int, index:int) -> list:
    # Inserts value into an array at specified index

    arr.insert(index,value)

    return (arr)

insert_into_array([2, 4, 8, 10], 6, 2)
# 12/04/2026 Daily Challenge

# Given a 2D matrix, return a flat array with all of its values in clockwise order.

"""
The returned array should have the top-left value first, move right along the top row, then down the right column,
then left along the bottom row, then up the left column. Repeat inward for any remaining layers.

"""

def spiral_matrix(matrix:list) -> list:

    # Define the new list to return:

    new_list = []

    # Loop over the first row:

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            



    print(new_list)

    return matrix

spiral_matrix([[25, 24, 23, 22, 21], [10, 9, 8, 7, 20], [11, 2, 1, 6, 19], [12, 3, 4, 5, 18], [13, 14, 15, 16, 17]])
# 12/04/2026 Daily Challenge

# Given a 2D matrix, return a flat array with all of its values in clockwise order.

"""
The returned array should have the top-left value first, move right along the top row, then down the right column,
then left along the bottom row, then up the left column. Repeat inward for any remaining layers.

"""

def spiral_matrix(matrix:list) -> list:

    # Define the new list to return:

    new_list = []

    while len(matrix) > 0: 

        # Get the first row and delete it from matrix:
        new_list.extend(matrix[0])
        del matrix[0]

        if len(matrix) == 0:
            break

        # Get the last column and delete it from matrix:
        for i in range(len(matrix)):
            new_list.append(matrix[i][-1])
            del matrix[i][-1]
            
        if len(matrix) == 0:
            break        

        # Get the last row reversed and delete it from matrix:
        new_list.extend(matrix[-1][::-1])
        del matrix[-1]

        if len(matrix) == 0:
            break

        # Get the first column reversed and delete it from matrix:
        for i in range(len(matrix)-1,-1,-1):
            new_list.append(matrix[i][0])
            del matrix[i][0]

        if len(matrix) == 0:
            break

    print(new_list)
    return new_list

spiral_matrix([["a", "b", "c", "d"], ["l", "m", "n", "e"], ["k", "p", "o", "f"], ["j", "i", "h", "g"]])
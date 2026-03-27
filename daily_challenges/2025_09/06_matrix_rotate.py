# 06/09/2025 Daily Challenge

# Given a matrix (an array of arrays), rotate the matrix 90 degrees clockwise and return it.
# For instance, given
# [1, 2],
# [3, 4],
# You should return
# [3, 1],
# [4, 2].

def rotate(matrix:list) -> list:

    # Rotate an array of arrays 90 degrees:

    new_matrix = []

    # Get the index sequence ([1][0],[0][0]) , ([1][1],[0][1])

    for i in range(len(matrix)):
        element = []
        for j in range(len(matrix[i])-1,-1,-1):
            element.append(matrix[j][i])
        new_matrix.append(element)

    return(new_matrix)
rotate([[1, 2], [3, 4]])
# 19/03/2026 Daily Challenge

# Given a matrix (an array of arrays) filled with two distinct values,
# return a new matrix where all occurrences of one value are swapped with the other.

def invert_matrix(matrix:list) -> list:

    # Capture the two different values:

    values = []
     
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if not matrix[i][j] in values:
                values.append(matrix[i][j])
    
    # Change the actual value for the opposite one:

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != values[0]:
                matrix[i][j] = values[0]
            else:
                matrix[i][j] = (values[1])
  
    return matrix

invert_matrix([["a", "b"], ["a", "a"]])
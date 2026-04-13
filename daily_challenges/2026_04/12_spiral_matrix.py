# 12/04/2026 Daily Challenge

# Given a 2D matrix, return a flat array with all of its values in clockwise order.

"""
The returned array should have the top-left value first, move right along the top row, then down the right column,
then left along the bottom row, then up the left column. Repeat inward for any remaining layers.

"""

def spiral_matrix(matrix:list) -> list:

    # Crear una nueva lista:
    new_list = []

    while True:

        # Coger la primera fila y eliminar:
        new_list.extend(matrix[0])
        matrix.remove(matrix[0])

        if len(matrix) == 0:
            break

        # Coger la ultima columna y eliminar:
        for i in range(len(matrix)):
            new_list.append(matrix[i][-1])
            matrix[i].remove(matrix[i][-1])
        
        if len(matrix) == 0:
            break
        
        # Coger la ultima fila reversed y eliminar
        new_list.extend(matrix[-1][::-1])
        matrix.remove(matrix[-1])

        if len(matrix) == 0:
            break

        # Coger la primera columna reversed y eliminar
        for i in range(len(matrix)-1,-1,-1):
            new_list.append(matrix[i][0])
            matrix[i].remove(matrix[i][0])
        
        if len(matrix) == 0:
            break

    print(new_list)

spiral_matrix([[True, False, False], [False, True, True], [False, True, False], [True, True, False]])


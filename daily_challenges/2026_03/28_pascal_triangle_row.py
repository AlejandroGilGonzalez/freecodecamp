# 28/03/2026 Daily Challenge

# Given an integer n, return the nth row of Pascal's triangle as an array.

# In Pascal's Triangle, each row begins and ends with 1,
# and each interior value is the sum of the two values directly above it.

# Here's the first 5 rows of the triangle:

"""
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1

"""

def pascal_row(number:int) -> list:

    # Stablish the starting sequence:

    start = [[1],[1,1]]

    # Sum the numbers with their preceding ones to create a new row, the number of times needed:
    
    for i in range(number-1): # Number of rows needed.
        if len(start[i]) >= 2: # Skiping the first number.
            new_row = [1,1]
            for j in range(len(start[i])-1): # Iterating over each number of each row.
                element = start[i][j] + start[i][j+1] # Summing the first with the second and so on.
                new_row.insert(j+1,element)
            start.append(new_row)

    
    return(start[number-1])

pascal_row(10)
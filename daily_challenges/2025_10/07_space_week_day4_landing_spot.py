# 07/10/2025 Daily Challenge

# In day four of Space Week, you are given a matrix of numbers (an array of arrays),
# representing potential landing spots for your rover. Find the safest landing spot based on the following rules:

"""
- Each spot in the matrix will contain a number from 0-9, inclusive.
- Any 0 represents a potential landing spot.
- Any number other than 0 is too dangerous to land. The higher the number, the more dangerous.
- The safest spot is defined as the 0 cell whose surrounding cells (up to 4 neighbors, ignore diagonals) have the lowest total danger.
- Ignore out-of-bounds neighbors (corners and edges just have fewer neighbors).
- Return the indices of the safest landing spot. There will always only be one safest spot.

"""

def find_landing_spot(matrix:list) -> list:

    # Stablish a list of indexes and their counter:
    counters_list = []

    print()
    # For each number 0 check the surrounding numbers:
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Stablish a counter for each index:
            counter = 0
            if matrix[i][j] == 0:
                # Sum the neighbours:
                if j+1 <= len(matrix[i]) - 1:
                    counter += matrix[i][j+1]
                if j-1 >= 0:
                    counter += matrix[i][j-1]
                if i+1 <= len(matrix) - 1:
                    counter += matrix[i+1][j]
                if i-1 >= 0:
                    counter += matrix[i-1][j]

                # Append the index and it's counter to the counters list:
                counters_list.append([[i,j],counter])

    # Compare the counters and get the index with the lowest counter:
    counters_list = sorted(counters_list, key= lambda x: x[1])

    return counters_list[0][0]

find_landing_spot([[1, 2, 1], [0, 0, 2], [3, 0, 0]])
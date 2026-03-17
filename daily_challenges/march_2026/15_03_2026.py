# 15/03/2026 Daily Challenge

# Given an array of strings representing chess pieces you still have on the board,
# calculate the value of the pieces your opponent has captured.

def get_captured_value(pieces:list) -> int or str:

    # Calculate the starting total value:

    starting_value = 39

    # Stablish starting values:

    values = [1,5,3,3,9,0]
    elements = {
        "P":8,
        "R":2,
        "N":2,
        "B":2,
        "Q":1,
        "K":1
    }
    
    # Count the number of pieces missing for replacing in dictionary:
    for key,val in elements.items():
        if not key in pieces:
            elements[key] = 0
    for p in pieces:
        term = pieces.count(p)
        elements[p] = term
    # Calculate the actual value of pieces:
 
    result = []
    for k,v in zip(values,elements.values()):
        result.append(k*v)

    suma = sum(result)

    # Rest the actual value to the starting value and getting the result:

    total_value = starting_value - suma        

    if elements["K"] == 0:
        return "Checkmate"
    else:
        return (total_value)
        
get_captured_value(["P", "P", "P", "P", "P", "R", "B"])
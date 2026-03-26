# 12/03/2026 Daily Challenge

# Given a 2D array representing a sequence of dominoes, determine whether it forms a valid chain.

def is_valid_domino_chain(dominoes:list)-> bool:
    # Getting the second number of dominoe(i) and first number of dominoe (i+1)

    result = True

    for i in range(len(dominoes)-1):
        dominoe = dominoes[i]
        next_dominoe = dominoes[i+1]
        if dominoe[1] == next_dominoe[0]:
            pass
        else:
            return (False)
    return (result)

is_valid_domino_chain([[1, 3], [3, 6], [6, 5]])
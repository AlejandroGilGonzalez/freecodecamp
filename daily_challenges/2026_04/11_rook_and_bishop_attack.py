# 11/04/2026 Daily Challenge

# Given a string for the location of a rook on a chess board, and another 
# for the location of a bishop, determine if one piece can attack another.

"""

A standard chessboard is 8x8, with columns labeled A through H (left to right)
and rows labeled 1 through 8 (bottom to top). It looks like this:

- Rooks can move as many squares as they want in a horizontal or vertical direction.
- Bishops can move as many squares as they want in any diagonal direction.
- One piece can attack another if it can move to the location of that piece.

Return:

- "rook" if the rook can attack the bishop.
- "bishop" if the bishop can attack the rook.
- "neither" if neither piece can attack one another.

"""

def rook_bishop_attack(rook:str, bishop:str) -> str:

    # Stablish a list of letters

    letters = ["A","B","C","D","E","F","G","H"]

    # Stablish the posible ranges:

    letters_range = abs(letters.index(rook[0]) - letters.index(bishop[0]))
    numbers_range = abs(int(rook[1]) - int(bishop[1]))

    # When letters have the same index or numbers are equal, return rook::

    if rook[0] == bishop[0] or rook[1] == bishop[1]:
        return "rook"
    
    # When letters range == to numbers range, return bishop:

    elif letters_range == numbers_range:
        return "bishop"
    
    # When neither can attack one other return "neither":

    else:
        return "neither"

rook_bishop_attack("C3", "F6")
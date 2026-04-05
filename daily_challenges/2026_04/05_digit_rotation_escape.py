# 05/04/2026 Daily Challenge

# Given a positive integer, determine if it, or any of its rotations, is evenly divisible by its digit count.

# A rotation means to move the first digit to the end. For example, after 1 rotation, 123 becomes 231.

"""
Check rotation 0 (the given number) first.
Given numbers won't contain any zeros.
Return the first rotation number if one is found, or "none" if not.

"""

def get_rotation(number:int) ->int:

    # Rotate the number and get the rotations needed:

    rotation = 0

    for i in range(len(str(number))):

        # First check for rotation 0:

        if number % len(str(number)) == 0:
            return (rotation)

        # Then rotate the number until we get the result 0:
        
        else:
            number = str(number)
            number = int(number[1:] + number[0])
            rotation += 1
    
    return ("none")

get_rotation(24681)
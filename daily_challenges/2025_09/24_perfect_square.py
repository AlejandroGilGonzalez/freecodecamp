# 24/09/2025 Daily Challenge

# Given an integer, determine if it is a perfect square.

# A number is a perfect square if you can multiply an integer by itself to achieve the number.
# For example, 9 is a perfect square because you can multiply 3 by itself to get it.

def is_perfect_square(number:int) -> bool:

    # Loop over every number in range of the given number:

    for i in range(number+1):

        # If any number multiplied by itself is equal to the given number return True:

        if i * i == number:
            return True

        # Else return False

    return False

is_perfect_square(25281)
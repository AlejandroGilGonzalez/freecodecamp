# 04/04/2026 Daily Challenge

# Given a string representing a math equation, determine whether it is correct.

"""
The left side may contain up to three positive integers and the operators +, -, *, and /.

The equation will be given in the format: "number operator number = number"
(with two or three numbers on the left). For example: "2 + 2 = 4" or "2 + 3 - 1 = 4".

The right side will always be a single integer.

Follow standard order of operations: multiplication and division are evaluated before addition and subtraction, from left-to-right.

"""
import re

def is_valid_equation(equation:str) -> bool:

    # Search for the numbers in the equation and convert them to integers:

    numbers = re.search(r"(.+)(?=.*=)", equation)
    
    eq = numbers.group(1)

    # Search for the result in the equation:

    total = re.search(r"(?<=\=\s)(\d+)", equation)
    total = int(total.group(1))

    # Evaluate multiplication and division:

    eq_result = eval(eq)
  
    # Evaluate if total of the equation is equal to result:

    if eq_result == total:
        return True
    else:
        return False

is_valid_equation("10 - 6 / 2 + 8 * 3 = 31")
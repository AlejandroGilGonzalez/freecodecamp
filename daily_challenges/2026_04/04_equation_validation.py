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

    numbers = re.findall(r"(\d+)(?=.*=)", equation)

    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    

    # Search for the result in the equation:

    total = re.search(r"(?<=\=\s)(\d+)", equation)
    total = int(total.group(1))

    # Search for the operators in the equation:

    operators = re.findall(r"([\+\/\-\*])", equation)

    # Evaluate multiplication:

    for i in range(len(operators)):
        if "*" in operators:
            position = operators.index("*") # Gets the operator index
            result = numbers[position] * numbers[position+1] # Does the operation with the same index number and the next one.
            numbers[position] = result # Converts the number to the result
            numbers.remove(numbers[position+1]) # Removes the number we don't need anymore
            operators.remove(operators[position])

    # Evaluate division:

        elif "/" in operators:
            position = operators.index("/")
            result = numbers[position] / numbers[position+1]
            numbers[position] = result
            numbers.remove(numbers[position+1])
            operators.remove(operators[position])

    # Evaluate last sum:
        
        elif "+" in operators:
            position = operators.index("+")
            result = numbers[position] + numbers[position+1]
            numbers[position] = result
            numbers.remove(numbers[position+1])
            operators.remove(operators[position])
    
    # Evaluate substraction:

        elif "-" in operators:
            position = operators.index("-")
            result = numbers[position] - numbers[position+1]
            numbers[position] = result
            numbers.remove(numbers[position+1])
            operators.remove(operators[position])

    # Evaluate if total of the equation is equal to result:
    
    if int(numbers[0]) == total:
        return True
    else:
        return False

is_valid_equation("5 + 2 + 3 = 10")
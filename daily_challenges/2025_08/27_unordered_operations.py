# Daily Challenge 27/08/2025

# Given an array of integers and an array of string operators, apply the operations to the numbers 
# sequentially from left-to-right. Repeat the operations as needed until all numbers are used. Return the final result.

"""
For example, given [1, 2, 3, 4, 5] and ['+', '*'], 
return the result of evaluating 1 + 2 * 3 + 4 * 5 from 
left-to-right ignoring standard order of operations.

"""

def evaluate(numbers:list, operators:list) -> int:

    # Use the first given operator with the first 2 numbers:

    operator = 0
    
    result = 0

    # Iter over the numbers list:
    
    for i in range(len(numbers)):

        # The first result is the operation between first two numbers:

        if i == 0:
            if operators[operator] == "+":
                result += numbers[i] + numbers[i+1]
                operator +=1
            elif operators[operator] == "-":
                result += numbers[i] + numbers[i+1]
                operator +=1
            elif operators[operator] == "*":
                result += numbers[i] * numbers[i+1]
                operator +=1
            elif operators[operator] == "/":
                result += numbers[i] / numbers[i+1]
                operator +=1
            elif operators[operator] == "%":
                result += numbers[i] % numbers[i+1]
                operator +=1
        
        # The second number must not be used anymore:

        elif i == 1:
            continue

        # The rest is used in sequence:

        else:

            # When the operator is sum:
            
            if operators[operator] == "+":
                result += numbers[i]
                
            # When the operator is substract:

            elif operators[operator] == "-":
                result -= numbers[i]
                
            # When the operator multiplies:

            elif operators[operator] == "*":
                result *= numbers[i]
                
            # When the operator dvidies:

            elif operators[operator] == "/":
                result /= numbers[i]

            # When the operator returns the rest of a division:

            elif operators[operator] == "%":
                result %= numbers[i]

            # Restart operators when we reached the last one: 

            if len(operators) > operator + 1:
                operator +=1
            else:
                operator = 0
            
    return (result)

evaluate([11, 4, 10, 17, 2], ['*', '*', '%'])
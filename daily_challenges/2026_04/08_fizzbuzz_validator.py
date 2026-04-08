# 08/04/2026 Daily Challenge

# Given an array of sequential integers, with multiples of 3 and 5 replaced, determine if it's a valid FizzBuzz sequence.

"""
In a valid FizzBuzz sequence:

Multiples of 3 are replaced with "Fizz".
Multiples of 5 are replaced with "Buzz".
Multiples of both 3 and 5 are replaced with "FizzBuzz".
All other numbers remain as integers.

"""

def is_fizz_buzz(numbers:list) -> bool:

    # Get the first number and it's position:

    for i in range(len(numbers)):
        if type(numbers[i]) == int:
            number = numbers[i]
            position = numbers.index(numbers[i])
            break
    
    # Get the entire sequence:

    sequence = []

    for i in range(len(numbers)):
        if i < position:
            result = number - (position - i)
            sequence.append(result)
        elif i == position:
            sequence.append(number)
        else:
            result = sequence[i-1] + 1
            sequence.append(result)

    # Check if the original sequence is valid:

    for i in range(len(numbers)):
        
        if sequence[i] % 5 == 0 and sequence[i] % 3 == 0:
            if numbers[i] != "FizzBuzz":
                return False
        elif sequence[i] % 5 == 0:
            if numbers[i] != "Buzz":
                return False
        elif sequence[i] % 3 == 0:
            if numbers[i] != "Fizz":
                return False

    return True

is_fizz_buzz(["FizzBuzz", 16, 17, "Fizz", 19, "Buzz"])
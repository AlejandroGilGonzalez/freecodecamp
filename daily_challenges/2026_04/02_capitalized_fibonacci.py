# 02/04/2026 Daily Challenge

# Given a string, return a new string where each letter is capitalized if its index is a Fibonacci number, and lowercased otherwise.
#
# The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. 
#
# The first character is at index 0.
#
# If the index of non-letter characters is a Fibonacci number, leave it unchanged.

def capitalize_fibonacci(phrase:str) -> str:

    # Get a list of fibonacci numbers depending on the length of the string:

    fibonacci = [0,1]

    for i in range(len(phrase)):
        new = fibonacci[i] + fibonacci[i+1]
        fibonacci.append(new)

    # Create a new string for capitalize letters if their index is a fibonacci number:

    new_string = ""

    # Capitalize or lower the letters depending on their index:

    for i, char in enumerate(phrase):
        if i in fibonacci:
            new_string += char.upper()
        elif not i in fibonacci:
            new_string += char.lower()

    return new_string

capitalize_fibonacci("hello world")
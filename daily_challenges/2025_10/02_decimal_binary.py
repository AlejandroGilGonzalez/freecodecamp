# 02/10/2025 Daily Challenge

# Given a non-negative integer, return its binary representation as a string.

"""
A binary number uses only the digits 0 and 1 to represent any number.
To convert a decimal number to binary, repeatedly divide the number by 2 and record the remainder.
Repeat until the number is zero. Read the remainders last recorded to first. For example, to convert 12 to binary:

"""

def to_binary(decimal:int) -> str:

    # Get the reminders as a string:

    reminders = ""

    # Divide the number by 2 until number is 0:

    while decimal != 0:
        reminders += str(decimal % 2)
        decimal = decimal // 2

    reminders = reminders[::-1]

    return reminders

to_binary(12)
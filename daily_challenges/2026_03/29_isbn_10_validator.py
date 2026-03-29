# 29/03/2026 Daily Challenge

# Given a string, determine if it's a valid ISBN-10.

"""
An ISBN-10 consists of hyphens ("-") and 10 other characters. After removing the hyphens ("-"):

The first 9 characters must be digits, and
The final character may be a digit or the letter "X", which represents the number 10.

To validate it:

Multiply each digit (or value) by its position (multiply the first digit by 1, the second by 2, and so on).
Add all the results together.
If the total is divisible by 11, it's valid.

"""

def is_valid_isbn10(isbn:str) -> bool:

    # Remove the hyphens from the string:

    isbn = isbn.replace("-","")

    # Determine if the 9 first digits are numbers: 

    try:
        int(isbn[:9])
    except:
        return False

    # Put every digit on a list for better indexation:

    isbn = list(isbn)

    # Determine if the 10th digit is a number or "X":
    
    if isbn[9] != "X" and isbn[9] not in "0123456789":
        return False
    
    # If it's "X" replace it by 10:

    if isbn[9] == "X":
        isbn[9] = "10"
        
    # Digit validation:

    # Multiply each digit by it's position and add the result together:

    result = 0

    for i in range(len(isbn[:10])):
        result += int(isbn[i]) * (i+1)
    
    # Return True if the total is divisible by 11, else return False:

    if result % 11 == 0:
        return True
    else:
        return False

is_valid_isbn10("0-8044-2957-X")
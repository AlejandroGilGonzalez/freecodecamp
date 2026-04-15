# 03/10/2025 Daily Challenge

# Given a password string, return "weak", "medium", or "strong" based on the strength of the password.

"""
A password is evaluated according to the following rules:

- It is at least 8 characters long.
- It contains both uppercase and lowercase letters.
- It contains at least one number.
- It contains at least one special character from this set: !, @, #, $, %, ^, &, or *.

Return "weak" if the password meets fewer than two of the rules.
Return "medium" if the password meets 2 or 3 of the rules.
Return "strong" if the password meets all 4 rules.

"""
import string

def check_strength(password:str) -> str:

    # Add a counter for the number of strengths:
    strength_counter = 0

    # Evaluate if the password follows 8 characters length:
    if len(password) >= 8:
        strength_counter += 1
    

    # Evaluate if contains both upper and lower characters:
    upper = False
    lower = False

    for char in password:
        if char.isalpha():
            if char in string.ascii_lowercase:
                lower = True
            elif char in string.ascii_uppercase:
                upper = True

    if upper and lower:
        strength_counter +=1

    # Evaluate if it contains at least one number:
    for char in password:
        if char.isnumeric():
            strength_counter +=1
            break
    
    # Evaluate if it contains at least one special character:
    special = "!@#$%^&*"
    for char in password:
        if char in special:
            strength_counter += 1
            break
    
    # Return the strength of the given password:
    if strength_counter < 2:
        return ("weak")
    elif strength_counter in range(2,4):
        return ("medium")
    elif strength_counter >= 4:
        return ("strong")

check_strength("PASSWORD!")
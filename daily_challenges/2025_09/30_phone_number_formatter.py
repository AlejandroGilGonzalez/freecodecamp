# 30/09/2025 Daily Challenge

# Given a string of eleven digits, return the string as a phone number in this format: "+D (DDD) DDD-DDDD".

def format_number(number:str) -> str:

    # Give the number the specified format:

    result = f"+{number[0]} ({number[1:4]}) {number[4:7]}-{number[7:]}"

    return result

format_number("15554354792")
# 05/09/2025 Daily Challenge

"""
Given a string, determine if it is a valid IPv4 Address.
A valid IPv4 address consists of four integer numbers
separated by dots (.). Each number must satisfy the following conditions:

- It is between 0 and 255 inclusive.
- It does not have leading zeros (e.g. 0 is allowed, 01 is not).
- Only numeric characters are allowed.

"""
import re

def is_valid_ipv4(ipv4:str) -> bool:

    
    # Create a list of the numbers with the given string:

    ipv4_numbers = re.findall(r"(\d+)", ipv4)

    # Check if there is a non-numeric character:

    for item in ipv4_numbers:
        if not item.isdigit():
            return False
    
    # Check if there is the correct ammount of numbers:

    if len(ipv4_numbers) != 4:
        return False

    # Before converting to integer, check if any string number has leading zeros:

    for item in ipv4_numbers:
        hasleading_zeros = item.startswith("0") and len(item) > 1
        if hasleading_zeros == True:
            return False
    
    # Check if there is a dot "." in the required positions:
    
    ipv4_positions = re.findall(r"(\d+|\.)", ipv4)

    for i in range(1,len(ipv4_positions),2):
        if ipv4_positions[i] not in ".":
            return (False)

    # Convert the numbers to integer:

    for i in range(len(ipv4_numbers)):
        ipv4_numbers[i] = int(ipv4_numbers[i])
    
    # Check if the numbers position satisfies the conditions:

    for i in range(0,len(ipv4_numbers),2):
        if ipv4_numbers[i] < 0 or ipv4_numbers[i] > 255:
            return False

    # If every position is correct return True

    return (True)

is_valid_ipv4("192.168.101.")
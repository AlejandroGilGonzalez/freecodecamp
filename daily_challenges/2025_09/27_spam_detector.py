# 27/09/2025 Daily Challenge

# Given a phone number in the format "+A (BBB) CCC-DDDD", where each letter represents a digit as follows:

"""
- A represents the country code and can be any number of digits.
- BBB represents the area code and will always be three digits.
- CCC and DDDD represent the local number and will always be three and four digits long, respectively.

"""

# Determine if it's a spam number based on the following criteria:

"""
- The country code is greater than 2 digits long or doesn't begin with a zero (0).
- The area code is greater than 900 or less than 200.
- The sum of first three digits of the local number appears within last four digits of the local number.
- The number has the same digit four or more times in a row (ignoring the formatting characters).

"""
import re

def is_spam(tel_number:str) -> bool:

    # Get the country code:

    country_code = re.search(r"^\+(\d+)", tel_number)
    country_code = country_code.group(1)

    # Get the area code:

    area_code = re.search(r"\((\d+)\)", tel_number)
    area_code = area_code.group(1)

    # Get the local number:

    local_number = re.search(r"(\d{3}\-\d{4})", tel_number)
    local_number = local_number.group(1)

    # Country code must be at most 2 digits long and begin with a 0:

    if len(country_code) > 2:
        return True
    
    if country_code[0] != "0":
        return True

    # Area code must be in range 200 - 900:

    if int(area_code) not in range(200,901):
        return True

    # The sum of the first three digits in local number can't appear within the last four digits:

    three_digits = [int(x) for x in local_number[:3]]

    sum_three_digits = sum(three_digits)

    if str(sum_three_digits) in local_number[4:]:
        return True

    # The number cannot have the same digits 4 or more times in a row:

    all_digits = country_code + area_code + local_number.replace("-","")

    counter = 1

    for i in range(1,len(all_digits)):
        if all_digits[i] == all_digits[i-1]:
            counter +=1
        else:
            counter = 1

        if counter >= 4:
            return True

    return False

is_spam("+00 (555) 234-0182")
# 12/08/2025 Daily Challenge

# Given a string representing a number,
# and an integer base from 2 to 36, determine whether the number is valid in that base.

def is_valid_number(num:str, base:int):

    try:
        int(num,base)
        return True
    except:
        return False

is_valid_number("10201", 2)
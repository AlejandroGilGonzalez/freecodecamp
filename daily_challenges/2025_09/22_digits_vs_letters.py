# 22/09/2025 Daily Challenge

# Given a string, return "digits" if the string has more digits than letters,
# "letters" if it has more letters than digits, and "tie" if it has the same amount of digits and letters.

# Digits consist of 0-9.
#
# Letters consist of a-z in upper or lower case.
#
# Ignore any other characters.

def digits_or_letters(battle:str) -> str:

    # Counts the numbers and letters and adds to the counter:

    numbers = 0
    letters = 0

    for i in range(len(battle)):
        if battle[i].isalpha():
            letters += 1
        elif battle[i].isnumeric():
            numbers += 1
        else:
            continue

    # Compares the counters to extract the winner:

    if numbers > letters:
        return "digits"
    elif letters > numbers:
        return "letters"
    elif letters == numbers:
        return "tie" 

digits_or_letters("a1b2c3d")
# 12/09/2026 Daily Challenge

"""
Given an input array of seven integers, representing a week's time,
where each integer is the amount of hours spent on your phone that day,
determine if it is too much screen time based on these constraints:

- If any single day has 10 hours or more, it's too much.
- If the average of any three days in a row is greater than or equal to 8 hours, it’s too much.
- If the average of the seven days is greater than or equal to 6 hours, it's too much.

"""

def too_much_screen_time(hours:list) -> bool:

    # Determine if any single day has 10 hours or more:

    for i in range(len(hours)):
        if hours[i] >= 10:
            return True

    # Determine if the average of any 3 days in a row has more or equal to 8 hours:

    for i in range(len(hours)-2):
        if (hours[i] + hours[i+1] + hours[i+2]) / 3 >= 8:
            return True
        
    # Determine if the average of 7 days is greater or equal to 6 hours:

    if sum(hours) / 7 >= 6:
        return True

    return False

too_much_screen_time([1, 2, 3, 4, 5, 6, 7])
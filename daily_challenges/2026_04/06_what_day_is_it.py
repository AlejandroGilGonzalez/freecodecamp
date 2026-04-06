# 06/04/2026 Daily Challenge

# Given a Unix timestamp in milliseconds, return the day of the week.

"""
Valid return days are:

"Sunday"
"Monday"
"Tuesday"
"Wednesday"
"Thursday"
"Friday"
"Saturday"
Be sure to ignore time zones.

"""
from datetime import datetime

def get_day_of_week(timestamp:int) -> str:

    # Convert timestamp in miliseconds to datetime object:

    date = datetime.fromtimestamp(timestamp / 1000)
    
    # Get the day of the week from the datetime object:

    day_week = date.strftime("%A")

    return (day_week)

get_day_of_week(1775492249000)
# 30/03/2026 Daily Challenge

# Given a date string, return the date 9 months in the future.
#
# The given and return strings have the format "YYYY-MM-DD".
#
# If the month nine months into the future doesn't contain the original day number, return the last day of that month.

from datetime import datetime

def get_due_date(date_str:str) -> str:

    # Convert the given string to datetime:

    start_date = datetime.strptime(date_str, "%Y-%m-%d")

    # Get the months that have 30 or 31 days: 

    month_30 = [4,6,9,11]
    month_31 = [1,3,5,7,8,10,12]

    # Sum the 9 months in the different posibilities: 

    

    if start_date.month + 9 > 12: # When the sum gets you to the next year:
        year = start_date.year + 1 # Sums one year.
        month = abs (12 - (start_date.month + 9)) # Gets the month difference

    else: # When the sum gets you to the same year:
        year = start_date.year
        month = start_date.month + 9

    # When February get the same day or max day

    if month == 2 and start_date.day > 28: 
        day = 28
    elif month == 2 and start_date.day < 28:
        day = start_date.day

    # For the rest of months gets the same day if it cans, if not the maximum.

    elif start_date.day > 30 and month in month_30:
        day = 30
    else:
        day = start_date.day

    # Replaces the starting date with the new date

    new_date = start_date.replace(year=year,month=month,day=day)
    
    # Returns the result as string not time object:

    result = datetime.strftime(new_date,"%Y-%m-%d")

    return (result)
    


get_due_date("2026-10-11")
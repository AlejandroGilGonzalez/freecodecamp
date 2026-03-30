from datetime import datetime
import calendar

def get_due_date(date_str:str) -> str:

    # Converts the given string to a time object

    start_date = datetime.strptime(date_str, "%Y-%m-%d")

    # Sums 9 months to the given date:

    year = start_date.year + (start_date.month + 9 - 1 ) // 12 # Sums one year if needed
    month = (start_date.month + 9 - 1 ) % 12 + 1 # Gets the exact month
    day = min(start_date.day, calendar.monthrange(year,month)[1]) # Gets the max day

    # Replaces the starting date with the updated one

    new_date = start_date.replace(year=year, month=month, day=day)

    # Returns the new date as a string not time object
        
    new_date = datetime.strftime(new_date,"%Y-%m-%d")

    return (new_date)
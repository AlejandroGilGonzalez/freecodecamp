from datetime import datetime
import calendar

def get_due_date(date_str:str) -> str:

    start_date = datetime.strptime(date_str, "%Y-%m-%d")

    year = start_date.year + (start_date.month + 9 - 1 ) // 12
    month = (start_date.month + 9 - 1 ) % 12 + 1
    day = min(start_date.day, calendar.monthrange(year,month)[1])

    new_date = start_date.replace(year=year, month=month, day=day)
    
    new_date = datetime.strftime(new_date,"%Y-%m-%d")

    return (new_date)
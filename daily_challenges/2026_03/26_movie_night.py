# 26/03/2026 Daily Challenge

# Given a string for the day of the week, another string for a showtime,
# and an integer number of tickets, return the total cost of the movie tickets for that showing.

# The showtime will be given in the format "H:MMam" or "H:MMpm". For example "10:00am" or "10:00pm".

"""
Return the total cost in the format "$D.CC" using these rules:

Weekend (Friday - Sunday): $12.00 per ticket.
Weekday (Monday - Thursday): $10.00 per ticket.
Matinee (before 5:00pm): subtract $2.00 per ticket (except on Tuesdays).
Tuesdays: all tickets are $5.00 each.

"""
from datetime import datetime

def get_movie_night_cost(day:str, showtime:str, number_of_tickets:int) -> str:

    # Define weekdays and weekend:

    weekdays = ["Monday","Tuesday","Wednesday","Thursday"]
    weekend = ["Friday","Saturday","Sunday"]

    # Define if showtime is on matinee or not:
    
    cost = 0

    showtime = datetime.strptime(showtime,"%I:%M%p")

    if showtime < datetime.strptime("05:00pm","%I:%M%p"):
        if day != "Tuesday":
            cost -= 2 * number_of_tickets

    # Return the total cost if weekends:

    if day in weekend:
        cost += 12 * number_of_tickets
        result = (f"${cost}.00")

    # Return the total cost if weekday:

    if day in weekdays and day != "Tuesday":
        cost += 10 * number_of_tickets
        result = f"${cost}.00"
    elif day == "Tuesday":
        cost += 5 * number_of_tickets
        result = f"${cost}.00"

    return(result)

get_movie_night_cost("Sunday", "10:00am", 1)

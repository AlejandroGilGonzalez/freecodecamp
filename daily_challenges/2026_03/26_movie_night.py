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

def get_movie_night_cost(day:str, showtime:str, number_of_tickets:int) -> str:

    # Define weekdays and weekend:

    weekdays = ["Monday","Tuesday","Wednesday","Thursday"]
    weekend = ["Friday","Saturday","Sunday"]

    # Define if showtime is on matinee or not:

    matinee = False
    showtime = showtime.split(":")
    
    if int(showtime[0]) >= 5 and "am" in showtime[1]:
        matinee = True
    elif int(showtime[0]) < 5 and "pm" in showtime[1]:
        matinee = True

    # Return the total cost if weekends:

    if day in weekend:
        cost = 12 * number_of_tickets
        if matinee:
            cost -= 2 * number_of_tickets
        result = (f"${cost}.00")

    # Return the total cost if weekday:

    if day in weekdays and day != "Tuesday":
        cost = 10 * number_of_tickets
        if matinee:
            cost -= 2 * number_of_tickets
        result = f"${cost}.00"
    elif day == "Tuesday":
        cost = 5 * number_of_tickets
        result = f"${cost}.00"

    return(result)

get_movie_night_cost("Monday", "4:30am", 1)

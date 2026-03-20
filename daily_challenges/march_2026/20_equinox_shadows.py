# 20/03/2026 Daily Challenge

"""
Today is the equinox, when the sun is directly above the equator and perfectly 
overhead at noon. Given a time, determine the shadow cast by a 4-foot vertical pole.

The time will be a string in "HH:MM" 24-hour format (for example, "15:00" is 3pm).
You will only be given a time in 30 minute increments.
Rules:

The sun rises at 6am directly "east", and sets at 6pm directly "west".
A shadow always points opposite the sun.
The shadow's length (in feet) is the number of hours away from noon, cubed.
There is no shadow before sunrise (before 6am), after sunset (6pm or later), or at noon.
Return:

If a shadow exists, return "(length)ft (direction)". For example, "8ft west".
Otherwise, return "No shadow".

For example, given "10:00", return "8ft west" because 10am is 2 hours from noon,
so 23 = 8 feet, and the shadow points west because the sun is in the east at 10am.

"""

from datetime import datetime,time,timedelta

def get_shadow(given_hour:str) -> str:

    # Convert the given string and noon into time objects for hour and minute:

    given_hour = datetime.strptime(given_hour,"%H:%M")
    noon = datetime.strptime("12:00","%H:%M")
    sunrise = datetime.strptime("06:00","%H:%M")
    sunset = datetime.strptime("18:00","%H:%M")

    # Stablish the non-shadow moments:

    if given_hour < sunrise:
        return "No shadow"
    if given_hour == noon:
        return "No shadow"
    if given_hour >= sunset:
        return "No shadow"

    # Stablish the time span and shadows:

    if noon < given_hour:
        time_span = given_hour - noon
        shadow = "east"
    elif noon > given_hour:
        time_span = noon - given_hour
        shadow = "west"
    
    # Convert the time span to total seconds:

    total = int(time_span.total_seconds())

    # Convert to hours and cube it for knowing the total ft:

    total_hours = total / 3600
    
    total_ft = total_hours**3

    if total % 3600 == 0:
        total_ft = int(total_ft)

    result = str(str(total_ft) + "ft" + " " + shadow)
    
    return result

get_shadow("10:00")
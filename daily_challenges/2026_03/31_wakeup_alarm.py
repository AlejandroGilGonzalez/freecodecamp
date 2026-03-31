# 31/03/2026 Daily Challenge

# Given a string representing the time you set your alarm and a string representing
# the time you actually woke up, determine if you woke up early, on time, or late.
#
# Both times will be given in "HH:MM" 24-hour format.

"""
Return:

"early" if you woke up before your alarm time.
"on time" if you woke up at your alarm time, or within the 10 minute snooze window after the alarm time.
"late" if you woke up more than 10 minutes after your alarm time.
Both times are on the same day.

"""

from datetime import datetime, timedelta

def alarm_check(alarm_time:str, wake_time:str) -> str:

    # Convert the given strings to time objects:

    alarm_time = datetime.strptime(alarm_time, "%H:%M")
    wake_time = datetime.strptime(wake_time,"%H:%M")

    # Convert the time objects to time delta:

    new_alarm_time = timedelta(hours= alarm_time.hour, minutes = alarm_time.minute)
    new_wake_time = timedelta(hours= wake_time.hour, minutes = wake_time.minute)

    # Get the total minutes difference, in positive or negative integer:

    minutes_diff = int((new_wake_time.total_seconds() - new_alarm_time.total_seconds()) / 60)
    
    print (minutes_diff)

    # Return 'early' if wake time is before alarm time so minutes are negative:

    if minutes_diff < 0:
        return "early"

    # Return 'on time' if wake time is 10 minutes or less from alarm time:

    elif minutes_diff <= 10:
        return "on time"

    # Check if wake time is more than 10 minutes after the alarm time:

    elif minutes_diff > 10:
        return "late"

alarm_check("07:00", "06:45")
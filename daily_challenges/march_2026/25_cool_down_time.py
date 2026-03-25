# 25/03/2026 Daily Challenge

# Given two timestamps, the first representing when a user finished an exam,
# and the second representing the current time, determine whether the user can take an exam again.

"""
Both timestamps will be given the format: "YYYY-MM-DDTHH:MM:SS",
for example "2026-03-25T14:00:00". Note that the time is 24-hour clock.

A user must wait at least 48 hours before retaking an exam.

"""

import datetime

def can_retake(finish_time, current_time):

    # Change the given format to datetime object:

    finish_time = finish_time.replace("T"," ")
    finish_time = datetime.datetime.strptime(finish_time,"%Y-%m-%d %H:%M:%S")
    current_time = current_time.replace("T"," ")
    current_time = datetime.datetime.strptime(current_time,"%Y-%m-%d %H:%M:%S")

    # Get the interval hours between the current and the finish time:

    interval = current_time - finish_time
    
    hour_interval = interval.total_seconds() / 3600

    # Return true when interval is greater than 48h cool down time:

    if hour_interval >= 48:
        return True
    else:
        return False

can_retake("2026-03-23T08:00:00", "2026-03-25T14:00:00")
# 21/08/2025 Daily Challenge

# Given a number of miles ran, and a time in "MM:SS" (minutes:seconds) it took
# to run those miles, return a string for the average time it took to run each mile in the format "MM:SS".

import re
from datetime import datetime,time

def mile_pace(miles:int, duration:str) -> str:

    # Convert the minutes:seconds into seconds:
    
    minutes = re.search(r"(\d+):",duration)
    minutes = int(minutes.group(1))
    seconds = re.search(r":(\d+)",duration)
    seconds = int(seconds.group(1))

    total_seconds = minutes*60 + seconds

    # Get the average mile per second:

    average_time = total_seconds/miles
    
    # Get the average minutes and average seconds:

    av_minutes = int(average_time // 60)
    av_seconds = int(average_time % 60)
    total_time = time(av_minutes,av_seconds)
 
    # Convert it into str format:

    result = total_time.strftime("%H:%M")

    return (result)


mile_pace(26.2, "120:35")
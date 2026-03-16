# 13/03/2026 Daily Challenge

# Given two strings representing the time you parked your car 
# and the time you picked it up, calculate the parking fee.

from datetime import datetime,timedelta

def calculate_parking_fee(park_time:str, pickup_time:str) -> str:

    # Convert the given strings to datetime objects:

    park_time = datetime.strptime(park_time,"%H:%M")
    pickup_time = datetime.strptime(pickup_time, "%H:%M")

    # Check if pick up time is overnight and get the total hours:
    
    midnight_fee = 0
    if pickup_time < park_time:
        pickup_time += timedelta(days=1)
        midnight_fee += 10
    
    total = pickup_time - park_time

    in_seconds = total.total_seconds()

    if in_seconds // 3600 != in_seconds / 3600:
        hours = int(in_seconds // 3600) + 1
    else:
        hours = int(in_seconds / 3600)
    
    # Get the rounded up hours to apply the fee:

    total_fee = (hours*3)+midnight_fee
    if total_fee < 5:
        total_fee = 5
    
    result = f"${total_fee}"

    return result

calculate_parking_fee("18:15", "01:30")
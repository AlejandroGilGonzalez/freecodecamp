# 26/09/2025 Daily Challenge

"""
Given an array of numbers representing the speed at which vehicles were observed traveling
and a number representing the speed limit, return an array with two items,
the number of vehicles that were speeding, followed by the average amount beyond the speed limit of those vehicles.

If there were no vehicles speeding, return [0, 0].

"""
import math

def speeding(speeds:list, limit:int):

    # Get the number of vehicles that were speeding:

    speeding_vehicles = 0

    # Get the difference between speed limit and infractors:

    beyond = 0

    for number in speeds:
        if number > limit:
            # Gets the difference and sums it to the beyond:

            diff = number - limit
            beyond += diff

            # Sums a speeding vehicle:
            speeding_vehicles += 1
    
    # Get the average speed infraction:

    if beyond > 0:
        average = beyond / speeding_vehicles
        average = math.floor(average*100) / 100
    else:
        average = 0

    # Return speeding vehicles and average:

    print ([speeding_vehicles,average])

speeding([50, 60, 55], 60)
# 06/10/2025 Daily Challenge

"""
For day three of Space Week, you are given an array of numbers representing distances (in kilometers)
between yourself, satellites, and your home planet in a communication route. Determine how long it will take
a message sent through the route to reach its destination planet using the following constraints:

- The first value in the array is the distance from your location to the first satellite.
- Each subsequent value, except for the last, is the distance to the next satellite.
- The last value in the array is the distance from the previous satellite to your home planet.
- The message travels at 300,000 km/s.
- Each satellite the message passes through adds a 0.5 second transmission delay.
- Return a number rounded to 4 decimal places, with trailing zeros removed.

"""

def send_message(routes:list) -> float:

    # Define the velocity in km/s:
    velocity = 300000

    # Calculate how much it takes to each position and add it to the seconds counter:
    seconds = 0

    for i in range(len(routes)):
        seconds += routes[i]/velocity
        # For each movement but the last one, add 0.5 seconds delay:
        if not i == len(routes) - 1:
            seconds += 0.5
    
    # Round the given seconds to 4 decimals:

    result = round(seconds,4)

    return result

send_message([54600000, 54600000])
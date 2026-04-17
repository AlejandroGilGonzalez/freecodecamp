# 05/10/2025 Daily Challenge

"""
For the second day of Space Week, you are given a string where each character represents
the luminosity reading of a star. Determine if the readings have detected an exoplanet using the transit method.
The transit method is when a planet passes in front of a star, reducing its observed luminosity.

- Luminosity readings only comprise of characters 0-9 and A-Z where each reading corresponds to the following numerical values:
- Characters 0-9 correspond to luminosity levels 0-9.
- Characters A-Z correspond to luminosity levels 10-35.

A star is considered to have an exoplanet if any single reading is less than or equal to 80% of the average of all readings.
For example, if the average luminosity of a star is 10, it would be considered to have a exoplanet if any single reading is 8 or less.

"""
import string

def has_exoplanet(readings:str) -> bool:

    # Get a list of numbers and letters:
    digits = "0123456789" + string.ascii_uppercase

    # Get the index of each digit and the average:
    summing = 0

    for digit in readings:
        summing += digits.index(digit)

    average = summing / len(readings)
  
    # If any single reading is 80% or less return true:
    for digit in readings:
        if digits.index(digit) <= average * 0.8:
            return (True)

    return False

has_exoplanet("665544554")
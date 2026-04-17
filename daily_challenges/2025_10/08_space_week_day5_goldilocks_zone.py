# 08/10/2025 Daily Challenge

# For the fifth day of Space Week, you will calculate the "Goldilocks zone" of a star - 
# the region around a star where conditions are "just right" for liquid water to exist.

# Given the mass of a star, return an array with the start and end distances of its Goldilocks Zone in Astronomical Units.

"""
To calculate the Goldilocks Zone:

- Find the luminosity of the star by raising its mass to the power of 3.5.
- The start of the zone is 0.95 times the square root of its luminosity.
- The end of the zone is 1.37 times the square root of its luminosity.
- Return the distances rounded to two decimal places.

"""
from math import sqrt

def goldilocks_zone(mass:int) -> list:

    # Find the luminosity of the star by raising its mass to the power of 3.5
    luminosity = mass ** 3.5

    # Find the start of the zone by multiplying the square root of its luminosity by 0.95
    start_zone = round(sqrt(luminosity) * 0.95, 2)

    # Find the end of the zone by multiplying the square root of its luminosity by 1.37
    end_zone = round(sqrt(luminosity) * 1.37, 2)

    # Return each distance rounded to two decimals
    result = [start_zone, end_zone]
    
    return result

goldilocks_zone(0.5)
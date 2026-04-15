# 04/10/2025 Daily Challenge

# October 4th marks the beginning of World Space Week. The next seven days will bring you astronomy-themed coding challenges.

# For today's challenge, you are given the surface temperature of a star in Kelvin (K) 
# and need to determine its stellar classification based on the following ranges:

"""
- "O": 30,000 K or higher
- "B": 10,000 K - 29,999 K
- "A": 7,500 K - 9,999 K
- "F": 6,000 K - 7,499 K
- "G": 5,200 K - 5,999 K
- "K": 3,700 K - 5,199 K
- "M": 0 K - 3,699 K

Return the classification of the given star.

"""

def classification(temp:int) -> str:

    # Set the classification and temperature ranges in a dictionary:
    ranges = {
        "B":[10000,29999],
        "A":[7500,9999],
        "F":[6000,7499],
        "G":[5200,5999],
        "K":[3700,5199],
        "M":[0,3699]
    }

    # Loop over each classification to check if the given temperature enters in those ranges:
    for key, value in ranges.items():
        if temp in range(value[0],value[1]+1):
            return key

    # If the given temperature is greater than 29,999 return "O":
    if temp >= 30000:
        return "O"

classification(5778)
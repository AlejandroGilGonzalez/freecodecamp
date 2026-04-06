# 15/09/2025 Daily Challenge

# Given the current temperature of a room and a target temperature,
# return a string indicating how to adjust the room temperature based on these constraints:

"""
Return "heat" if the current temperature is below the target.
Return "cool" if the current temperature is above the target.
Return "hold" if the current temperature is equal to the target.
"""

def adjust_thermostat(temp:int, target:int) -> str:

    if target > temp:
        return "heat"
    elif target < temp:
        return "cool"
    else:
        return "hold"
    
adjust_thermostat(72, 72)


# 18/09/2025 Daily Challenge

# Given the size of a fuel tank, the current fuel level, and the price per gallon, return the cost to fill the tank all the way.

"""
- tankSize is the total capacity of the tank in gallons.
- fuelLevel is the current amount of fuel in the tank in gallons.
- pricePerGallon is the cost of one gallon of fuel.
- The returned value should be rounded to two decimal places in the format: "$d.dd".

"""

def cost_to_fill(tank_size:int, fuel_level:int, price_per_gallon:float) -> str:

    # Gets the remaining litres to fullfil:

    remaining = tank_size - fuel_level

    # Multiplies the price per gallon to the remaining litres to fullfil:

    cost = remaining * price_per_gallon

    print(cost)
    # Returns the total cost as string with 2 decimals in format "$d.dd":
    round_cost = "{:.2f}".format(cost)

    return f"${round_cost}"

cost_to_fill(20, 0, 4.00)
# 28/08/2025 Daily Challenge

# Given an array of integers representing the price of different laptops, and an integer representing your budget, return:

"""
1. The second most expensive laptop if it is within your budget, or
2. The most expensive laptop that is within your budget, or
3. 0 if no laptops are within your budget.

Duplicate prices should be ignored.

"""

def get_laptop_cost(laptops:list, budget:int) -> int:

    # Determine which laptops are in budget:

    in_budget = []

    for item in laptops:
        if item <= budget:
            in_budget.append(item)
    
    # Create a set with laptops prices in order:

    sorted_laptops = sorted(set(laptops))

    # If you can't afford any, return 0:

    if len(in_budget) == 0:
        return 0
    
    # Return the second most expensive if it is in budget:

    elif sorted_laptops[-2] <= budget:
        return sorted_laptops[-2]
    
    # If not, return the most expensive you can afford:

    elif sorted_laptops[-2] > budget:
        return max(sorted(set(in_budget)))
    

get_laptop_cost([2099, 1599, 1899, 1499], 2200)
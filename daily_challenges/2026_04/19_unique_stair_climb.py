# 19/04/2026 Daily Challenge

# Given a number of stairs, return how many distinct ways someone can climb them taking either 1 or 2 steps at a time.

def get_unique_climbs(steps:int) -> int:
    
    # Stablish a list of possibilities:
    posible_paths = []

    # Try every possibility:
    posible = []
    for i in range(steps):
        if sum(posible) + 2 <= steps:
            posible.append(2)
        elif sum(posible) + 1 <= steps:
            posible.append(1)
    if not posible in posible_paths:
        posible_paths.append(posible)



    return steps

get_unique_climbs(4)
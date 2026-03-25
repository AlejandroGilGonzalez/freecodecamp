# 06/03/2026 Daily Challenge

# Given an array of strings representing your trail map,
# return a string of the moves needed to get to your goal.

"""
The given strings will contain the values:

"C": Your current location
"G": Your goal
"T": Traversable parts of the trail
"-": Untraversable parts of the map

Return a string with the moves needed to follow the trail from your location to your goal where:

"R" is a move right

"D" is a move down

"L" is a move left

"U" is a move up

There will always be a single continuous trail, without any branching, from your current location to your goal.

Each trail location will have a maximum of two traversable locations touching it.

"""

def navigate_trail(maped:list) -> str:

    # Get the starting position:

    for i, pos in enumerate(maped):
        if "C" in pos:
            c_position = [i,pos.index("C")] # Starting position

    # Determine the total steps to make:
    total_steps = 0

    for level in maped:
        for char in level:
            if "T" in char or "G" in char:
                total_steps += 1

    # Function for returning string changes:

    def changed (phrase:list, ce:str, position:list) -> str:
        phrase[position[0]] = phrase[position[0]][:position[1]] + ce + phrase[position[0]][position[1]+1:]
        return phrase

    
    movements = ""

    # Determine the steps:
    for i in range(total_steps):
        # Moving Right:
        if "T" in maped[c_position[0]][c_position[1]+1] or "G" in maped[c_position[0]][c_position[1]+1]:
            movements += "R"
            c_position[1] += 1
            maped = changed(maped,"C",c_position)

        # Moving Left:
        elif c_position[1]-1 >= 0 and ("T" in maped[c_position[0]][c_position[1]-1] or "G" in maped[c_position[0]][c_position[1]-1]):
            movements += "L"
            c_position[1] -= 1
            maped = changed(maped,"C",c_position)

        # Moving Upwards:
        elif c_position[0]-1 >= 0 and ("T" in maped[c_position[0]-1][c_position[1]] or "G" in maped[c_position[0]-1][c_position[1]]):
            movements += "U"
            c_position[0] -= 1
            maped = changed(maped,"C",c_position)

        # Moving Downwards:
        elif "T" in maped[c_position[0]+1][c_position[1]] or "G" in maped[c_position[0]+1][c_position[1]]:
            movements += "D"
            c_position[0] += 1
            maped = changed(maped,"C",c_position)


    return(movements)

navigate_trail(["TTTTTTT-", "T-----T-", "T-----T-", "TTTT--TG", "---C----"])
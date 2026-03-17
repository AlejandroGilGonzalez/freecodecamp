# 24/08/2025 Daily Challenge

""" Given two strings representing your army and an opposing army, 
each character from your army battles the character at the same 
position from the opposing army using the following rules:"""

# Characters a-z have a strength of 1-26, respectively.
# Characters A-Z have a strength of 27-52, respectively.
# Digits 0-9 have a strength of their face value.
# All other characters have a value of zero.
# Each character can only fight one battle.

def battle(my_army:str, opposing_army:str) -> str:
    
    # Defining the characters:
    
    characters = "abcdefghijklmnopqrstuvwxyz"
    characters += characters.upper()

    # Define each battle in a tupple:
    
    battles = list(zip(my_army,opposing_army))

    # Get the result from each battle and count the number of victories:

    my_wins = 0
    opp_wins = 0

    for i in range(len(battles)):
        a,b = battles[i]
        if a in "0123456789":
            a = int(a)
        elif a in characters:
            a = characters.index(a)
        else:
            a = 0
        if b in "0123456789":
            b = int(b)
        elif b in characters:
            b = characters.index(b)
        else:
            b = 0

        if a > b:
            my_wins+=1
        elif a < b:
            opp_wins+=1

    print(my_wins)
    print(opp_wins)
    quit()
    # Define the conditions:

    if len(my_army) > len(opposing_army):
        return "Opponent retreated"
    elif len(my_army) < len(opposing_army):
        return "We retreated"
    elif my_wins > opp_wins:
        return "We won"
    elif my_wins < opp_wins:
        return "We lost"
    elif my_wins == opp_wins:
        return "It was a tie"


    return my_army

battle("pizza", "salad")
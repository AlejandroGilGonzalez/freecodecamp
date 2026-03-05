# 04/03/2026 Daily Challenge

# Given an array of playing cards, return a new array with the numeric value of each card.

"""
- Card Values:
    An Ace ("A") has a value of 1.
    Numbered cards ("2" - "10") have their face value: 2 - 10, respectively.
    Face cards: Jack ("J"), Queen ("Q"), and King ("K") are each worth 10.
- Suits:
    Each card has a suit: Spades ("S"), Clubs ("C"), Diamonds ("D"), or Hearts ("H").

- Card Format:
    Each card is represented as a string: "valueSuit". For Example: "AS" is the Ace of Spades, "10H" is the Ten of Hearts, and "QC" is the Queen of Clubs.
"""

def card_values(cards):
    """
    Finds the numeric value of iterables in a list
    """
    card_values = []
    
    for items in cards:
        if "A" in items[0]:
            card_values.append(1)
        elif items[0] in "JQK":
            card_values.append(10)
        else:
            if len(items) < 3:
                new = int(items[0])
            else:
                new = int(items[0:2])
            card_values.append(new)
    return (card_values)

card_values(["AS", "10S", "10H", "6D", "7D"])
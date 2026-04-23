# 20/04/2026 Daily Challenge

# Given a string representing an acronym, return the full name of the organization it belongs to from the list below:

"""
"National Avocado Storage Authority"
"Cats Infiltration Agency"
"Fluffy Beanbag Inspectors"
"Department Of Jelly"
"Wild Honey Organization"
"Eating Pancakes Administration"

Each letter in the given acronym should match the first letter of each word in the organization it belongs to, in the same order.

"""

def find_org(acronym:str) -> str:

    # Create a dictionary with all organizations:
    dictionary = {
        "1":"National Avocado Storage Authority",
        "2":"Cats Infiltration Agency",
        "3":"Fluffy Beanbag Inspectors",
        "4":"Department Of Jelly",
        "5":"Wild Honey Organization",
        "6":"Eating Pancakes Administration"
    }

    # Look for each item in the dictionary if the first word matches the first letter of acronym:
    for key, value in dictionary.items():

        # Split each name into pieces:
        split_value = value.split()

        # Look only for those who have the same length as the acronym:
        if len(split_value) == len(acronym):

            # Set a counter for knowing how many letters match with the acronym:
            counter = len(acronym)

            # Loop over the acronym letters and the name first letters,
            # If letters match, modify the counter:
            for i in range(len(acronym)):
                if acronym[i] == split_value[i][0]:
                    counter -= 1

            # Whenever counter is 0 means all words match with the acronym,
            # Then we return the organizations name:
            if counter == 0:
                return(value)

find_org("FBII")
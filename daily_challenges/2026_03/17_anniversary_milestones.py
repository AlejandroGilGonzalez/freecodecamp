# 17/03/2026 Daily Challenge

# Given an integer representing the number of years a couple has been married,
# return their most recent anniversary milestone according to this chart:

"""
1  "Paper"
5  "Wood"
10  "Tin"
25	"Silver"
40	"Ruby"
50	"Gold"
60	"Diamond"
70	"Platinum"

"""

# If they haven't reached the first milestone, return "Newlyweds".

def get_milestone(years:int) -> str:

    # Define the possible anniversary milestones in a dictionary:

    milestones = {
        1:"Paper",
        5:"Wood",
        10:"Tin",
        25:"Silver",
        40:"Ruby",
        50:"Gold",
        60:"Diamond",
        70:"Platinum"
    }

    if years < 1:
        return "Newlyweds"
    
    for key,values in milestones.items():
        if years >= key:
            result = milestones[key]
        else:
            break
    
    return(result)
    

get_milestone(8)
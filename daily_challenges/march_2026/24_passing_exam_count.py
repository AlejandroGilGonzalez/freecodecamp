# 24/03/2026 Daily Challenge

# Given an array of student exam scores and the score needed to pass it,
# return the number of students that passed the exam.

def passing_count(scores:list, passing_score:int) -> int:

    # Determine how many scores are able to pass the exam:
    count = 0
    for num in scores:
        if num >= passing_score:
            count += 1

    return(count)

passing_count([100, 80, 75, 88, 72, 74, 79, 71, 60, 92], 75)
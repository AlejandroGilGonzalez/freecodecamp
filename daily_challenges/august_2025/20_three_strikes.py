# 20/08/2025 Daily Challenge

# Given an integer between 1 and 10,000, return a count of how many numbers
# from 1 up to that integer whose square contains at least one digit 3.


def squares_with_three(number:int) -> int:
    
    # Returns the count of squared numbers that contains a 3:

    count = 0

    for i in range(1,number):
        if "3" in str(i**2):
            count+=1
            
    return (count)

squares_with_three(100)
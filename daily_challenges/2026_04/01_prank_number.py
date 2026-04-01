# 01/04/2026 Daily Challenge

# Given an array of numbers where all but one number follow a pattern,
# return a new array with the one number that doesn't follow the pattern fixed.

"""
The pattern will be one of:

The numbers increase from one to the next by a fixed amount (addition).
The numbers decrease from one to the next by a fixed amount (subtraction).
For example, given [2, 4, 7, 8, 10] return [2, 4, 6, 8, 10].

"""

def fix_prank_number(array:list) -> list:

    # Discover the pattern, comparing the results: 

    results = []

    # Try to substract the numbers and get a patterned result:
    #
    # If pattern number is negative the pattern is decreasing
    #
    # Otherwise it is increasing:

    for i in range(len(array)):
        try:
            sub = array[i+1] - array[i]
        except:
            break
        results.append(sub)

    print(results)

    # The only result that repeats is the difference:

    for result in results:
        if results.count(result) >= 2:
            patt_number = result

    print(patt_number)

    # If pattern number is positive, the pattern increases, otherwise decreases:

    if patt_number > 0:
        increase = True
    else:
        increase = False
    
    # Create a new pattern depending on where the pattern fails:

    new_pattern = []

    # When the pattern increases:

    if increase == True:

        # When the first number is correct we start at the first:

        if array[0] + patt_number == array[1]:
            new_pattern.append(array[0])
            for i in range(len(array)-1):
                new_number = new_pattern[i] + patt_number
                new_pattern.append(new_number)

        # When it is not correct, we start at the last:

        else:
            new_pattern.append(array[-1])
            for i in range(len(array)-1):
                new_number = new_pattern[i] - patt_number
                new_pattern.append(new_number)
            new_pattern.reverse()

    elif increase == False:

        # When the first number is correct we start at the first:

        if array[0] - abs(patt_number) == array[1]:
            new_pattern.append(array[0])
            for i in range(len(array)-1):
                new_number = new_pattern[i] - abs(patt_number)
                new_pattern.append(new_number)

        # When it is not correct, we start at the last:

        else:
            new_pattern.append(array[-1])
            for i in range(len(array)-1):
                new_number = new_pattern[i] + abs(patt_number)
                new_pattern.append(new_number)
            new_pattern.reverse()

    return (new_pattern)


fix_prank_number([4, 1, -2, -5, -8, -5])
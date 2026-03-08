try:
    goal = input("Your goal int: ")
    int(goal)
except ValueError:
    print("Must be a number")
else:
    print(goal)

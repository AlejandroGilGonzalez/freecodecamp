# 03/04/2026 Daily Challenge

# Given an array of browser commands, return an array with two values:
# the history as an array of URLs, and the index of the current page.

"""
Valid commands are:

"URL" - Where URL is a web address ("freecodecamp.org" for example).
Navigates to the given URL, adds it to the history at the next position, and discards any forward history.

"Back" - moves to the previous page in history, or stays on the current page if there isn't one.

"Forward" - moves to the next page in history, or stays on the current page if there isn't one.

"""

def get_browser_history(commands:list) -> list:

    # Add any web page navigated to the history:

    history = []

    # Control the path

    path = []

    # Stablish the position:

    position = 0

    for i in range(len(commands)):
        if "." in commands[i]:
            history.append(commands[i])
            print(history)
        # Adds or substract from the counter depending if back or forward

        if "Back" in commands[i]:
            path = history[:i-1]
            print(history)

        elif "Forward" in commands[i]:
            path = history[:i+1]
            print(history)

    result = [history,position]


get_browser_history(["example.com", "example.com/about", "Back", "example.com/contact", "example.com/blog", "Back", "Back", "Forward"])
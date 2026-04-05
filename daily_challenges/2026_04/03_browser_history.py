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

    # Add an index:

    index = 0
    
    for i in range (len(commands)):
        
        # Adding URLs:

        if "." in commands[i]:
            url = commands[i]
            history.append(url)
            index += 1

        # Moving back to the previous URL:

        elif "Back" in commands[i]:
            index -= 1
            history = history[:history.index(commands[i-1])]

        # When adding a web page we discard any forward history:

        elif "Forward" in commands[i]:
            index +=1
            
    print(index)


get_browser_history(["example.com", "example.com/about", "Back", "example.com/contact", "example.com/blog", "Back", "Back", "Forward"])
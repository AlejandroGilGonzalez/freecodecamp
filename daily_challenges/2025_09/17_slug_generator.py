# 17/09/2025 Daily Challenge

# Given a string, return a URL-friendly version of the string using the following constraints:

"""
- All letters should be lowercase.
- All characters that are not letters, numbers, or spaces should be removed.
- All spaces should be replaced with the URL-encoded space code %20.
- Consecutive spaces should be replaced with a single %20.
- The returned string should not have leading or trailing %20.

"""
import re

def generate_slug(url:str) -> str:

    # Removes leading or trailing spaces:

    url = url.strip()

    # Lowercases all letters:

    url = url.lower()

    # Removes special characters:

    url_only = re.findall(r"([\w\d\s])", url)

    url_only = "".join(url_only)

    # Single and consecutive spaces replaced by %20:

    # When there is more than one space:

    if url_only.count(" ") > 1:
        ws_indexes = [ind.start() for ind in re.finditer(r"\s", url_only)]
        url_only = url_only[:ws_indexes[0]] + "%20" + url_only[ws_indexes[1]+1:]
    
    # When there is a single space:
    else:
        url_only = url_only.replace(" ","%20")

    return url_only

generate_slug("  ?H^3-1*1]0!  W[0%R#1]D  ")
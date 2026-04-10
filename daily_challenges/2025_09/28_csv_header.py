# 28/09/2025 Daily Challenge

# Given the first line of a comma-separated values (CSV) file, return an array containing the headings.

# The first line of a CSV file contains headings separated by commas.
# Remove any leading or trailing whitespace from each heading.


def get_headings(csv):

    # Find all headings in csv file:

    headings = [head.strip() for head in csv.split(",")]

    return headings

get_headings("username , email , signup date ")
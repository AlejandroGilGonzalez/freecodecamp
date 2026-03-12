isbn = "132456789A0"

try:
    if len(isbn) == 10:
        isbn[0:10].isnumeric() == True
    else:
        test = isbn.isnumeric() == True
except ValueError:
    print("Invalid character was found.")
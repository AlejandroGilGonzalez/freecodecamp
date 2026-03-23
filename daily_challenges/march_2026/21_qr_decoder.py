# 21/03/2026 Daily Challenge

# Given a 6x6 matrix (array of arrays), representing a QR code, return the string of binary data in the code.

"""
# The QR code may be given in any rotation of 90 degree increments.

# A correctly oriented code has a 2x2 group of 1's (orientation markers)
# in the bottom-left, top-left, and top-right corners.

# The three 2x2 orientation markers are not part of the binary data.

# The binary data is read left-to-right, top-to-bottom (like a book)
# when the QR code is correctly oriented.

# A code will always have exactly one valid orientation.

"""
import re

def decode_qr(qr_code:list) -> str:

    # Define the correct orientation:

    new_order = []

    if qr_code[0][0:2] != "11" or qr_code[0][4:6] != "11":
        qr_code = qr_code[::-1]
        for code in qr_code:
            new_order.append(code[::-1])
    else:
        new_order = qr_code

    print(new_order)

    result = []

    for i, count in enumerate(new_order):
        if i == 0 or i == 1:
            result.append(count[2:4])
        elif i == 4 or i == 5:
            result.append(count[2:6])
        else:
            result.append(count)
    
    result = "".join(result)
    print(result)


decode_qr(["111100", "110001", "100011", "001101", "110011", "110011"])
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

def decode_qr(qr_code:list) -> str:

    # Analizar si el codigo está en la posición correcta.q
    while qr_code[0][0:2] != "11" or qr_code[0][4:6] != "11" or qr_code[1][0:2] != "11" or qr_code[1][4:6]!= "11" or qr_code[4][0:2]!= "11" or qr_code[5][0:2]!= "11":

    # Si no es correcto, girar el codigo y volver al paso 1.

        new_list = []

        for i in range(len(qr_code)-1,-1,-1):
            element = ""
            for j in range(len(qr_code[i])):
                element += qr_code[i][j]
            new_list.append(element)
        qr_code = new_list
        print(new_list)

    # Si está correcto, sacar los orientation markers.
    result = ""
    result += qr_code[0][2:4]
    result += qr_code[1][2:4]
    result += qr_code[2]
    result += qr_code[3]
    result += qr_code[4][2:6]
    result += qr_code[5][2:6]

    return(result)


decode_qr(["111100", "110001", "100011", "001101", "110011", "110011"])
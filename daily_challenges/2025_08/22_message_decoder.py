# 22/08/2025 Daily Challenge

# Given a secret message string,and an integer representing the number of letters
# that were used to shift the message to encode it, return the decoded string.

"""
A positive number means the message was shifted forward in the alphabet.
A negative number means the message was shifted backward in the alphabet.
Case matters, decoded characters should retain the case of their encoded counterparts.
Non-alphabetical characters should not get decoded.

"""

def decode(message:str, shift:int) -> str:

    # Get the full alphabet with uppercase included:

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    upper_alphabet = alphabet.upper()

    print(alphabet)
    # Get the encrypted alphabet where letters are shifted:

    # When shift is positive:

    encrypted_alphabet = alphabet[shift:]+alphabet[:shift]
    upper_encrypted = upper_alphabet[shift:]+upper_alphabet[:shift]

    # Get the message letters index in the new encrypted alphabet:

    decrypted_text = ""

    for char in message:
        if char in alphabet:
            new_char = alphabet[encrypted_alphabet.index(char)]
            decrypted_text += new_char
        elif char in upper_alphabet:
            new_char = upper_alphabet[upper_encrypted.index(char)]
            decrypted_text += new_char
        else:
            decrypted_text += char    

    return(decrypted_text)

decode("Zqd xnt njzx?", -1)
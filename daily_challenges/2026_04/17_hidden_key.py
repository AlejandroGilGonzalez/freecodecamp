# 17/04/2026 Daily Challenge

# Given an encoded string, decode it using an encryption key and return it.

"""
To find the key:

- Look at all daily challenges up to today whose challenge number is a multiple of 25 (including this one).
- Take the first letter from each of those challenge titles and combine them into a string.
- If the title starts with a non-letter, find its first letter.

To decode the message, go over each letter in the encoded message and:

- Look at the corresponding letter in the key (repeat the key if the message is longer than the key).
- Convert the key letter to its corresponding number: "A" = 1, "B" = 2, ..., "Z" = 26.
- Shift the encoded letter backward in the alphabet by that number.
- If the shift goes before "A", wrap around to "Z".

"""
import string

def decode(message:str) -> str:

    # Find the key from the daily's titles:
    key = "VLHCGMDLNH"

    # Stablish the alphabet:
    alphabet = string.ascii_uppercase

    # If message is longer than the key, repeat the key:
    while len(message) > len(key):
        key += key
    # Include spaces in the key:
    for i in range(len(message)):
        if not message[i].isalpha():
            key = key[:i] + " " + key [i:]
    
    # Stablish a decoded message var:
    decoded_message = ""
    # Loop over each word and each letter in the encoded message:
    for i in range(len(message)):
        if message[i].isalpha():
            # Look by index at the corresponding letter in the key:
            letter = key[i]
            
            # Convert the letter to its corresponding number:
            shift = alphabet.index(letter) + 1

            # Shift the encoded letter n times backwards in the alphabet:
            if alphabet.index(message[i]) - shift < 0:
                reminder = abs(alphabet.index(message[i]) - shift)
                result = len(alphabet) - reminder
            else:
                result = alphabet.index(message[i]) - shift

            decoded_letter = alphabet[result]

            decoded_message += decoded_letter

        # If character is space return as it is:
        else:
            decoded_message += message[i]

    print(decoded_message)

decode("YALLUT PQUMJP")
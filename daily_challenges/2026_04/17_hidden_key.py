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
    
    # Stablish a decoded message var:
    decoded_message = []
    
    # Split the encoded message into a list:
    encoded = message.split()

    # Loop over each letter in each word from the message:
    for word in encoded:
        for i in range(len(word)):
            decoded_word = ""
            # Look by index at the corresponding letter in the key:
            letter = key[i]

            # Get the letter index in the alphabet to stablish a shift:
            shift = alphabet.index(letter) + 1

            # Shift the encoded letter backwards in the alphabet by that number:
            # If the shift goes before A, start again from Z:
            if alphabet.index(word[i]) - shift < 0:
                shift = abs(alphabet.index(word[i]) - shift)
            
            decoded_letter = alphabet[::-1][shift]
            decoded_word += decoded_letter
        decoded_message.append(decoded_word)
            
    print(decoded_message)

        
        
        

    
    return ""

decode("W IQQURV UG I ZDMDTRV IVW JQDHY TMHSA QB")
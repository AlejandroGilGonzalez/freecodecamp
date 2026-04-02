# 31/08/2025 Daily Challenge

# Given a named CSS color string, generate a random hexadecimal (hex) color code that is dominant in the given color.

"""
The function should handle "red", "green", or "blue" as an input argument.

If the input is not one of those, the function should return "Invalid color".

The function should return a random six-character hex color code where the input color value is greater than any of the others.

Example of valid outputs for a given input:

Input	Output
"red"	"FF0000"
"green"	"00FF00"
"blue"	"0000FF"

"""

from random import randint

def generate_hex(color:str) -> str:

    # Define the valid colors:

    valid_colors = ["red","green","blue"]

    # Return "Invalid color" if color is not valid:

    if color not in valid_colors:
        return "Invalid color"

    # Generate random numbers for each color until the one we need is superior:

    while True:

        red = randint (0,255)
        green = randint (0,255)
        blue = randint (0,255)

        # Convert the numbers to hexadecimal:

        if color == "red":
            if red > green and red > blue:
                result = f"{red:02X}{green:02X}{blue:02X}"
                break
        elif color == "green":
            if green > red and green > blue:
                result = f"{red:02X}{green:02X}{blue:02X}"
                break
        elif color == "blue":
            if blue > red and blue > green:
                result = f"{red:02X}{green:02X}{blue:02X}"
                break

    return (result)

generate_hex("red")
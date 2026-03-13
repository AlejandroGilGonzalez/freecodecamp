# 02/03/2026 Daily Challenge

# Given a string, return the sum of its letters.


""" Letters are A-Z in uppercase or lowercase
    Letter values are: "A" = 1, "B" = 2, ..., "Z" = 26
    Uppercase and lowercase letters have the same value.
    Ignore all non-letter characters."""

def sum_letters(s:str) -> int:
    abc = "abcdefghijklmnopqrstuvwxyz"
    suma = 0
    for letter in s.lower():
        if letter in abc:
            suma += list(abc).index(letter) + 1
    return suma

sum_letters("Hello")
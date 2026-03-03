def sum_letters(s):
    abc = "abcdefghijklmnopqrstuvwxyz"
    suma = 0
    for letter in s.lower():
        if letter in abc:
            suma += list(abc).index(letter) + 1
    return suma

sum_letters("Hello")
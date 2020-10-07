import random

def loremIpsum(len):

    string = "i"
    letras = "abcdefghijklmnopqrstuvwxyz"

    while (len > 0):
        num = random.randit(letras.len())
        string += letras[num]
        len -= 1

    return string
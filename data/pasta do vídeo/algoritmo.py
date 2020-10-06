import random

def loremIpsum(len):

    string = ""
    letras = "abcdefghijklmnopqrstuvwxyz"
    n_letras = 26

    while (len > 0):
        num = random.randint(0, n_letras)
        string += letras[num]
        len -= 1

    return string

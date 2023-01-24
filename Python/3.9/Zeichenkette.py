import random as r
import string


def conc(n):
    letters = list(string.ascii_letters)
    out = ""
    for i in range(n):
        out += r.choice(letters)
    return out


print(conc(7))


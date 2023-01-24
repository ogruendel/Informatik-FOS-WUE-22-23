def fun(s):
    out = ""
    for (i, l) in enumerate(s):
        if i % 2 == 0:
            out += l
    return out


print(fun("Ich bin ein test"))

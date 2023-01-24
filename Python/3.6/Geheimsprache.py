out = ""
for i, w in enumerate(input("Satz: ").split(" ")):
    out += w[1:] + w[0] + "ay "
print(out)

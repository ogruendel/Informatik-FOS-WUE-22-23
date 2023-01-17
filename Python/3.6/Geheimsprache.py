s = input("Satz: ")
s = s.split(" ")
out = ""

for i, w in enumerate(s):
    w = w[len(w) - 1] + w
    w = w[:-1]
    out += w + "ay "

print(out)

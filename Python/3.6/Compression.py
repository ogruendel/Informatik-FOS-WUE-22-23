s = "AAAABBAAABB"
sc = ""
prev = s[0]
c = 0

for letter in s:
    if letter == prev:
        c += 1
        prev = letter
    else:
        sc += prev + str(c)
        c = 0
        prev = letter
print(sc)

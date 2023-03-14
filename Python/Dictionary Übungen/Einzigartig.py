s = input("Wort eingeben: ")
l = []
for i in s:
    if i not in l:
        l.append(i)

print(f'{s} hat {len(l)} einzigartige Zeichen')

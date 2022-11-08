personen = int(input("Anzahl Personen: "))
nächte = int(input("Anzahl Nächte: "))

if personen % 2 != 0:
    print(format((((personen - 1) / 2) * 70 + 50) * nächte, '.2f') + "€")
else:
    print(format((personen / 2 * 70) * nächte, '.2f') + "€")

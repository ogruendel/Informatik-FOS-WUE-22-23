personen = int(input("Anzahl Personen: "))

if personen % 2 != 0:
    print(format(((personen - 1) / 2) * 70 + 50, '.2f') + "€")
else:
    print(format(personen / 2 * 70, '.2f') + "€")

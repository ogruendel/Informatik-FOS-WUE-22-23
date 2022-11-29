# Das Programm soll den Zimmerpreis pro Nacht ermitteln. Einzelzimmer kosten 50 € pro Nacht, Doppelzimmer
# kosten 70 €. Vom Nutzer soll abgefragt werden, wie viele Personen ein Zimmer benötigen. Dabei sollen
# immer zwei Personen in einem Zimmer übernachten. Bei einer ungeraden Anzahl von Personen wird einem
# automatisch ein Einzelzimmer zugewiesen.

personen = int(input("Anzahl Personen: "))
naechte = int(input("Anzahl Nächte: "))

if personen % 2 != 0:
    preis = ((personen - 1) / 2) * 70 + 50
    print(format(preis * naechte, '.2f') + "€")
else:
    preis = (personen / 2) * 70
    print(format(preis * naechte, '.2f') + "€")

def geldrechnung(geld, preis):
    if geld == preis:
        print("Passend")
    elif geld >= preis:
        print("Rückgeld:", format(geld - preis, '.2f') + "€")
    else:
        print("Noch nicht genug Geld")
        geldrechnung(float(input("Geld einwerfen: ")), (preis - geld))


wahl = int(input("Wasser (1), Limo (2) oder Saft (3): "))

if wahl == 1:
    preis = .5
elif wahl == 2:
    preis = 1.0
else:
    preis = 2.0

geld = float(input("Geld einwerfen: "))

geldrechnung(geld, preis)

preis = float(input("Preis: "))
rabatt = int(input("Rabatt in Prozent: ")) / 100

if rabatt >= 1:
    print("Rabatt zu hoch, bitte neu anfangen.")
else:
    print("Preis:", preis - (preis * rabatt))

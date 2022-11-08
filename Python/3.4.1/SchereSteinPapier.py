import random

wahl = input("Schere, Stein oder Papier?: ")

if wahl == "Schere":
    zahl = 0
elif wahl == "Stein":
    zahl = 1
else:
    zahl = 2

zufall = random.randint(0, 2)

if zufall == zahl:
    print("Gleichstand")
elif zufall == 0 and zahl == 2:
    print("Du verlierst")
elif zufall == 1 and zahl == 0:
    print("Du verlierst")
elif zufall == 2 and zahl == 1:
    print("Du verlierst")
else:
    print("Du gewinnst")


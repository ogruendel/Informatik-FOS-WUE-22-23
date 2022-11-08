tipp = input("Erster Tipp (z.B.: 2:1): ")
ergebnis = input("Spielergebnis (z.B.: 2:1): ")

tipp = tipp.split(":")
ergebnis = ergebnis.split(":")

if tipp == ergebnis:
    print("3 Punkte")
elif (tipp[0] > tipp[1] and ergebnis[0] > ergebnis[1]) or (tipp[0] < tipp[1] and ergebnis[0] < ergebnis[1]):
    print("2 Punkte")
else:
    print("0 Punkte")

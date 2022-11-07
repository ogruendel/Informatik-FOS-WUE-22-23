# Erstellen der Variable 'aufgenommen' und Aufforderung an den Nutzer einen Wert in der Konsole einzugeben.
# input() muss zu einem Integer umgewandelt werden, da 'zahl' sonst ein String ist, mit dem nicht gerechnet werden kann
aufgenommen = int(input("Aufgenommene Menge an Alkohol in Gramm: "))

# Erstellen der Variable 'verteilungsfaktor' und Aufforderung an den Nutzer einen Wert in der Konsole einzugeben.
# Der Wert ist zunächst nur ein Buchstabe (m, f, k) und wird später einen Zahlenwert bekommen
verteilungsfaktor = input("Mann (m), Frau (f), Kind (k): ")

# Erstellen der Variable 'masse' und Aufforderung an den Nutzer einen Wert in der Konsole einzugeben.
# input() muss zu einem Integer umgewandelt werden, da 'zahl' sonst ein String ist, mit dem nicht gerechnet werden kann
masse = int(input("Gewicht in Kilogramm: "))

# Erstellen der Variable 'volumen' und Aufforderung an den Nutzer einen Wert in der Konsole einzugeben.
# input() muss zu einem Integer umgewandelt werden, da 'zahl' sonst ein String ist, mit dem nicht gerechnet werden kann
volumen = int(input("Volumen des Getränks in Milliliter: "))

# Erstellen der Variable 'volumenprozent' und Aufforderung an den Nutzer einen Wert in der Konsole einzugeben.
# input() muss zu einem Integer umgewandelt werden, da 'zahl' sonst ein String ist, mit dem nicht gerechnet werden kann
volumenprozent = int(input("Alkoholvolumenanteil in %: ")) / 100

# Erstellen der Variable 'dichte' und festlegen des Wertes auf 0.8g/ml
dichte = 0.8

# Festlegen des Verteilungsfaktors basiert darauf, ob die Berechnung für eine Frau (f), einen Mann (m) oder ein Kind (k) stattfinden soll
if verteilungsfaktor == "f":
    verteilungsfaktor = 0.6
elif verteilungsfaktor == "m":
    verteilungsfaktor = 0.7
elif verteilungsfaktor == "k":
    verteilungsfaktor = 0.8

# Erstellen der Variable 'alkoholkonzentration' und ausrechnen des Wertes
alkoholkonzentration = (volumen * volumenprozent * dichte) / (masse * verteilungsfaktor)

# Formatieren der Variable 'alkoholkonzentration' und drucken in die Konsole
print(format(alkoholkonzentration * 100, '.2f'), "Promille")

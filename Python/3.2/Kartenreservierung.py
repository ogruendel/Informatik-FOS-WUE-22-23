# Erstellen der Variable 'vorname' und Aufforderung an den Nutzer seinen Vornamen in der Konsole anzugeben
vorname = input("Vorname: ")

# Erstellen der Variable 'nachname' und Aufforderung an den Nutzer seinen Nachnamen in der Konsole anzugeben
nachname = input("Nachname: ")

# Erstellen der Variable 'karten' und Aufforderung an den Nutzer die gewünschte Kartenanzahl in der Konsole anzugeben
# Wichtig: Der eingegebene Wert wird zunächst als String gespeichert. Da man mit diesem Datentypen jedoch nicht rechnen kann, muss die input methode zu einem int (Integer) umgewandelt werden. Das passiert mit int()
karten = int(input("Anzahl Karten: "))

# Erstellen der Variable 'preis' und festlegen des Wertes auf 8
preis = 8

# Drucken der Variable 'vorname' in der Konsole
print("Vorname:", vorname)

# Drucken der Variable 'nachname' in der Konsole
print("Nachname", nachname)

# Drucken der Variable 'karte' in der Konsole
print("Anzahl bestellter Karten:", karten)

# Ausrechnen des Gesamtpreises (karten * preis) und formatieren auf 2 Nachkommastellen. Anschließendes drucken der Variable '' in der Konsole
print("Gesamtpreis:", format(preis * karten, '.2f'), "€")

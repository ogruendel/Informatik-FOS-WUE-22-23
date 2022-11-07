# Erstellen der Variable 'noten' als Listen Objekt
noten = [1, 3, 4, 3, 2, 1, 2, 3, 4, 5, 2, 1, 2, 3, 3, 2, 1, 4, 4]

# Erstellen der Variable 'durchschnitt' und ausrechnen des Notendurchschnitts
durchschnitt = sum(noten) / len(noten)

# Erstellen der Variable 'beste' und zuweisung des niedrigsten Wertes aus der Liste 'noten'
beste = min(noten)

# Erstellen der Variable 'schlechteste' und zuweisung des höchsten Wertes aus der Liste 'noten'
schlechteste = max(noten)

# Drucken der Variablen 'durchschnitt', 'beste' und 'schlechteste' in die Konsole
print(durchschnitt)
print(beste)
print(schlechteste)

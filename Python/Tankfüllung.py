# Erstellen der Variable 'werte' als Listen Objekt mit den vorgegebenen Werten
werte = [1020, 923, 780, 890]

# Erstellen der Variable 'durchschnitt' und Berechnung der durchschnittlichen Reichweite pro Tankfüllung.
# sum() zählt alle Werte einer Liste zusammen und len() gibt die Länge einer Liste wieder
durchschnitt = sum(werte) / len(werte)

# Drucken der durchschnittlichen Reichweite in die Konsole
print(durchschnitt)

# Berechnung des durchschnittlichen Benzinverbrauches auf 100 km.
# (70 / durchschnitt) liefert zurück, wie viele Liter Benzin man pro gefahrenen Kilometer verbrennt. * 100 liefert wie viel Liter Benzin man pro 100 gefahrene Kilometer verbrennt.
einhundert = (70 / durchschnitt) * 100

# Drucken des Benzinverbrauches auf 100 km in die Konsole
print(einhundert)

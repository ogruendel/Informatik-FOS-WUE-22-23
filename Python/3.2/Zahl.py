# Erstellen der Variable 'zahl'. input() muss zu einem Integer umgewandelt werden, da 'zahl' sonst ein String ist, mit dem nicht gerechnet werden kann
zahl = int(input("Eine Zahl, bitte: "))

# Wert von 'zahl' um 1 erhöhen
zahl += 1

# Wert von 'zahl' mit 2 multiplizieren
zahl *= 2

# Wert von 'zahl' um 1 verringern
zahl -= 1

# Quadrieren des Wertes von 'zahl'
zahl = zahl ** 2

# Drucken des Wertes von 'zahl' in die Konsole
print("Die Zahl lautet:", zahl)

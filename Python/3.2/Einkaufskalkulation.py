# Erstellen der Variable 'listeneinkaufspreis' und Aufforderung an den Nutzer einen Wert in der Konsole einzugeben.
# input() muss zu einem Integer umgewandelt werden, da 'zahl' sonst ein String ist, mit dem nicht gerechnet werden kann
listeneinkaufspreis = int(input("Listeneinkaufspreis: "))

# Erstellen der Variable 'bezugskosten' und Aufforderung an den Nutzer einen Wert in der Konsole einzugeben.
# input() muss zu einem Integer umgewandelt werden, da 'zahl' sonst ein String ist, mit dem nicht gerechnet werden kann
bezugskosten = int(input("Bezugskosten: "))

# Erstellen der Variable 'rabatt' und festlegen des Wertes auf 0.10 (10%)
rabatt = .1

# Erstellen der Variable 'sk' und festlegen des Wertes auf 0.02 (2%)
sk = .02

# Erstellen der Variable 'lieferrabatt' und ausrechnen des Wertes
lieferrabatt = rabatt * listeneinkaufspreis

# Erstellen der Variable 'zieleinkaufspreis' und ausrechnen des Wertes
zieleinkaufspreis = listeneinkaufspreis - lieferrabatt

# Erstellen der Variable 'skonto' und ausrechnen des Wertes
skonto = sk * zieleinkaufspreis

# Erstellen der Variable 'bareinkaufspreis' und ausrechnen des Wertes
bareinkaufspreis = zieleinkaufspreis - skonto

# Erstellen der Variable 'bezugspreis' und ausrechnen des Wertes
bezugspreis = bareinkaufspreis + bezugskosten

# Drucken aller Variablen in der Konsole
print("Listeneinkaufspreis:", format(listeneinkaufspreis, '.2f') + "€")
print("Lieferrabatt:", format(lieferrabatt, '.2f') + "€")
print("Zieleinkaufspreis:", format(zieleinkaufspreis, '.2f') + "€")
print("Skonto:", format(skonto, '.2f') + "€")
print("Bareinkaufspreis:", format(bareinkaufspreis, '.2f') + "€")
print("Bezugskosten:", format(bezugskosten, '.2f') + "€")
print("Bezugspreis:", format(bezugspreis, '.2f') + "€")

# Erstellen der Variable 'listeneinkaufspreis' und Aufforderung an den Nutzer einen Wert in der Konsole einzugeben.
# input() muss zu einem Integer umgewandelt werden, da 'zahl' sonst ein String ist, mit dem nicht gerechnet werden kann
listeneinkaufspreis = int(input("Listeneinkaufspreis: "))

# Erstellen der Variable 'bezugskosten' und Aufforderung an den Nutzer einen Wert in der Konsole einzugeben.
# input() muss zu einem Integer umgewandelt werden, da 'zahl' sonst ein String ist, mit dem nicht gerechnet werden kann
bezugskosten = int(input("Bezugskosten: "))

# Erstellen der Variable 'rabatt' und Aufforderung an den Nutzer einen Wert in der Konsole einzugeben. Anschließendes ausrechnen in Prozent
rabatt = int(input("Rabatt in Prozent: ")) / 100

# Erstellen der Variable 'sk' und Aufforderung an den Nutzer einen Wert in der Konsole einzugeben. Anschließendes ausrechnen in Prozent
sk = int(input("Skonto in Prozent: ")) / 100

# Erstellen der Variable 'ust' und festlegen des Wertes auf 0.19 (19%)
ust = .19

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

# Erstellen der Variable 'umsatzsteuer' und ausrechnen des Wertes
umsatzsteuer = ust * bezugspreis

# Erstellen der Variable 'bruttopreis' und ausrechnen des Wertes
bruttopreis = umsatzsteuer + bezugspreis

# Formatieren aller Variablen und anschließendes drucken in der Konsole
print("Listeneinkaufspreis:", format(listeneinkaufspreis, '.2f') + "€")
print("Lieferrabatt:", format(lieferrabatt, '.2f') + "€")
print("Zieleinkaufspreis:", format(zieleinkaufspreis, '.2f') + "€")
print("Skonto:", format(skonto, '.2f') + "€")
print("Bareinkaufspreis:", format(bareinkaufspreis, '.2f') + "€")
print("Bezugskosten:", format(bezugskosten, '.2f') + "€")
print("Bezugspreis:", format(bezugspreis, '.2f') + "€")
print("Umsatzsteuer:", format(umsatzsteuer, '.2f') + "€")
print("Bruttopreis:", format(bruttopreis, '.2f') + "€")

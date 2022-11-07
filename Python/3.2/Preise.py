# Erstellen der Variable 'brutto' und Aufforderung an den Nutzer eine Zahl in der Konsole einzugeben.
# input() muss zu einem Integer umgewandelt werden, da 'brutto' sonst ein String ist, mit dem nicht gerechnet werden kann
brutto = int(input("Bruttopreis: "))

# Erstellen einer Variablen 'netto' und ausrechnen des Nettopreises
netto = brutto / 1.19

# Formatieren des Nettopreises auf zwei Nachkommastellen und anschließendes Drucken der Variablen 'netto' in die Konsole
print(format(netto, '.2f') + "€")

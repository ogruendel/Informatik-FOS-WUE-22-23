# Importieren der Bibliothek 'random'
import random

# Erstellen der Variable 'geraten' als Listen Objekt, um eine Eingabe des Nutzers aufzurufen.
# Die input Methode muss zu einem Integer umgewandelt (gecastet) werden, da sonst die einzelnen Zahlen nicht den richtigen Typ hätten
geraten = [int(input("Bitte Zahl 1 eingeben: ")), int(input("Bitte Zahl 2 eingeben: ")), int(input("Bitte Zahl 3 eingeben: ")), int(input("Bitte Zahl 4 eingeben: ")), int(input("Bitte Zahl 5 eingeben: ")), int(input("Bitte Zahl 6 eingeben: "))]

# Erstellen der Variable 'lottozahlen' als Listen Objekt
lottozahlen = [random.randint(0, 49), random.randint(0, 49), random.randint(0, 49), random.randint(0, 49), random.randint(0, 49), random.randint(0, 49)]

print(geraten)
print(lottozahlen)

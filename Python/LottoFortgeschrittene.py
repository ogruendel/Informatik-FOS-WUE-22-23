# Importieren der Bibliothek 'random'
import random

# Erstellen der Variable 'geraten' als Listen Objekt, um eine Eingabe des Nutzers aufzurufen.
# Die input Methode muss zu einem Integer umgewandelt (gecastet) werden, da sonst die einzelnen Zahlen nicht den richtigen Typ hätten
geraten = [int(input("Bitte Zahl 1 eingeben: ")), int(input("Bitte Zahl 2 eingeben: ")), int(input("Bitte Zahl 3 eingeben: ")), int(input("Bitte Zahl 4 eingeben: ")), int(input("Bitte Zahl 5 eingeben: ")), int(input("Bitte Zahl 6 eingeben: "))]

# Erstellen der Variable 'lottozahlen' als Listen Objekt
lottozahlen = [random.randint(0, 49), random.randint(0, 49), random.randint(0, 49), random.randint(0, 49), random.randint(0, 49), random.randint(0, 49)]

# Erstellen der Variable 'richtig' um die Nummer der richtig geratenen Zahlen zu zählen
richtig = 0

# Die Methode .sort() sortiert alle Elemente einer liste nach steigender Reihenfolge (numerisch und alphabetisch)
geraten.sort()
lottozahlen.sort()

# Die for Schleife erhöht i jedes Mal um 1, solange 'i' kleiner der Anzahl an Elementen in der Liste 'lottozahlen' ist (5)
for i in range(len(lottozahlen)):

    # Das if Statement überprüft, ob das 'i'te' Element der Liste 'geraten' irgendwo in der Liste 'lottozahlen' vorkommt. Ist das der fall, wird die Variable 'richtig' um eins erhöht
    if geraten[i] in lottozahlen:
        richtig += 1

# Zum Schluss werden die generierten Zahlen, die geratenen Zahlen und die Anzahl an richtig geratener Zahlen in der Konsole gedruckt
print(lottozahlen)
print(geraten)
print(richtig)

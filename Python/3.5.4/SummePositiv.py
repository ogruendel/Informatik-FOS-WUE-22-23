summe = 0
for i in range(0, int(input("Wie häufig soll eine Summe gebildet werden: "))):
    summe += abs(int(input("Welche Zahl soll dazu gezählt werden: ")))

print(summe)

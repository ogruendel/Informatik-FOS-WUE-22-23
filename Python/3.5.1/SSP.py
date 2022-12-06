import random

geraten = input("Schere, Stein oder Papier: ")
richtig = ["schere", "stein", "papier"]

while geraten.lower() not in richtig:
    print("Keine Option")
    geraten = input("Schere, Stein oder Papier: ")

x = random.choice(richtig)

if geraten == x:
    print("Unentschieden")
elif geraten == "schere" and x == "papier":
    print("Gewonnen")
elif geraten == "stein" and x == "schere":
    print("Gewonnen")
elif geraten == "papier" and x == "stein":
    print("Gewonnen")
else:
    print("Verloren")

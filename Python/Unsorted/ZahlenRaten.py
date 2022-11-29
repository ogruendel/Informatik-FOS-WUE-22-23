import random

spieler1 = int(input("Spieler 1: Zahl zwischen 1 und 100: "))
spieler2 = int(input("Spieler 2: Zahl zwischen 1 und 100: "))
zufall = random.randint(1, 100)

print(f'Zufallszahl: {zufall}')

if abs(spieler1 - zufall) == abs(spieler2 - zufall):
    print("Unentschieden")
elif abs(spieler2 - zufall) > abs(spieler1 - zufall):
    print("Spieler 1 gewinnt")
else:
    print("Spieler 2 gewinnt")

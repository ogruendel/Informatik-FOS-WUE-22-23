kontostand = 136.34

print(f'Ihr Guthaben beträgt {kontostand} Euro')
abheben = float(input("Wie viel Geld möchten sie abheben? "))

if abheben <= kontostand:
    print(f'Es werden {abheben} Euro ausgezahlt')
else:
    print("Keine Auszahlung! Dieser Betrag übersteigt ihr Guthaben")


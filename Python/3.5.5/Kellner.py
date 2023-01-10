anzahl = int(input("Wie viele Kellner haben gearbeitet: "))
tische = int(input("Wie viele Tische gibt es: "))
umsatz = 0.0
for kellner in range(1, anzahl + 1):
    for tisch in range(1, tische + 1):
        umsatz += float(input(f'Kellner {kellner}, wie viel Umsatz haben sie an Tisch {tisch} gemacht: '))
print(f'Der gesamte Umsatz heute Abend beträgt: {format(umsatz, ",.2f")}€')

zahlen = float(input("Wie viel ist zu bezahlen?: "))
gezahlt = float(input("Wie viel hat der Kunde bezahlt?: "))

rückgeld = gezahlt - zahlen

if rückgeld < 0:
    print("Der Kunde hat zu wenig bezahlt.")
else:
    print("Der Kunde bekommt", str(format(rückgeld, '.2f')) + "€ Rückgeld")

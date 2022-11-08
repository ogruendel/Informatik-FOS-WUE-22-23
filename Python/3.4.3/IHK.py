punkte = int(input("Wie viele Punkte wurden erreicht?: "))

if punkte > 100:
    print("Ungültige Punktzahl")
elif punkte <= 29:
    print("Ungenügend")
elif punkte <= 49:
    print("Mangelhaft")
elif punkte <= 66:
    print("Ausreichend")
elif punkte <= 80:
    print("Befriedigend")
elif punkte <= 91:
    print("Gut")
else:
    print("Sehr Gut")

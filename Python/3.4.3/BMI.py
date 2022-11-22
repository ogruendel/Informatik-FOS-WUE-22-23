groesse = float(input("Größe in cm: ")) / 100
gewicht = float(input("Gewicht in Kilogramm: "))
geschlecht = input("Geschlecht? (m) oder (f): ")

bmi = round(gewicht / (groesse * groesse), 1)

if geschlecht == "m":
    if bmi < 20:
        print("BMI:", bmi, "Untergewicht")
    elif bmi > 25:
        print("BMI:", bmi, "Übergewicht")
    else:
        print("BMI:", bmi, "Normalgewicht")
else:
    if bmi < 19:
        print("BMI:", bmi, "Untergewicht")
    elif bmi > 24:
        print("BMI:", bmi, "Übergewicht")
    else:
        print("BMI:", bmi, "Normalgewicht")

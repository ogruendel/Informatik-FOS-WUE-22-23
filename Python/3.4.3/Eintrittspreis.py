alter = int(input("Alter: "))

if alter <= 2:
    print("Gratis")
elif alter <= 16:
    print(format(8 * .5, '.2f') + "€")
elif alter > 65:
    print(format(8 * .75, '.2f') + "€")
else:
    print("8.00€")

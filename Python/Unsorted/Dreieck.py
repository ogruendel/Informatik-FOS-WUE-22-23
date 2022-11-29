a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
dreieck = [a, b, c]
dreieck.sort()

if dreieck[2] < dreieck[0] + dreieck[1]:
    if dreieck.count(dreieck[1]) > 1 or dreieck.count(dreieck[2]) > 1:
        print("Gleichschenkliges Dreieck")
        exit()
    elif (dreieck[0] * dreieck[0]) + (dreieck[1] * dreieck[1]) == (dreieck[2] * dreieck[2]):
        print("Rechtwinkliges Dreieck")
        exit()
    print("Dreieck")
else:
    print("Kein Dreieck")

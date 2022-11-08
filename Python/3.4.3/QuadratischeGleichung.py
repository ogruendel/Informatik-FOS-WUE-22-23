import math

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

x1 = (-b + math.sqrt((b * b) - (4 * a * c))) / 2 * a
x2 = (-b - math.sqrt((b * b) - (4 * a * c))) / 2 * a

if b * b - (4 * a * c) == 0:
    print("Eine Lösung:")
    print("x =", x1)
elif b * b - (4 * a * c) < 0:
    print("Keine Lösung!")
else:
    print("Zwei Lösungen:")
    print("x1 =", x1)
    print("x2 =", x2)

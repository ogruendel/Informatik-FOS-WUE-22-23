# Erstellen der Variable 'r' und Aufforderung an den Nutzer einen Wert in der Konsole einzugeben. Anschließendes ausrechnen auf einen Wert zwischen 0 und 1 (Maximaler Ursprungswert: 255)
r = int(input("R: ")) / 255

# Erstellen der Variable 'g' und Aufforderung an den Nutzer einen Wert in der Konsole einzugeben. Anschließendes ausrechnen auf einen Wert zwischen 0 und 1 (Maximaler Ursprungswert: 255)
g = int(input("G: ")) / 255

# Erstellen der Variable 'b' und Aufforderung an den Nutzer einen Wert in der Konsole einzugeben. Anschließendes ausrechnen auf einen Wert zwischen 0 und 1 (Maximaler Ursprungswert: 255)
b = int(input("B: ")) / 255

# Erstellen der Variable 'k' und ausrechnen des Wertes
k = 1 - max(r, g, b)

# Erstellen der Variable 'c' und ausrechnen des Wertes
c = (1 - r - k) / (1 - k)

# Erstellen der Variable 'm' und ausrechnen des Wertes
m = (1 - g - k) / (1 - k)

# Erstellen der Variable 'y' und ausrechnen des Wertes
y = (1 - b - k) / (1 - k)

# Drucken der Variablen 'c', 'm', 'y' und 'k' in der Konsole
print("C:", c)
print("M:", m)
print("Y:", y)
print("K:", k)

mail = "Tonys-Tiernahrung@web.de"
mail2 = "info@Wellesittich-Rudy.de"
lieferanten = []
lieferant_neu = ["hundebedarf", "wuerzburg.com"]
print(mail.split('@')[0])
print(mail2.split('.')[0].split('@')[1])
lieferanten.append(mail)
lieferanten.append(mail2)
lieferanten.append(lieferant_neu[0] + "@" + lieferant_neu[1])
print(lieferanten)

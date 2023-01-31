usr = "OliverGruendel"
pin = "0123"
bal = 1000
attempts = 0
loggedIn = False


def menu():
    print("Menu:\n")
    print("Kontostand (1)")
    print("Geld auszahlen (2)")
    print("Beenden (3)")
    return int(input())


def checkbal():
    print(f"Ihr Kontostand beträgt: {bal}€")


def withdraw(bal):
    towithdraw = int(input("Wie viel Euro möchten sie abheben? "))
    if towithdraw > bal or towithdraw % 5 != 0:
        print("Ungültiger Betrag!")
        return bal
    else:
        return bal - towithdraw


if input("Bitte geben Sie ihren Benutzernamen ein: ") == usr:
    while not loggedIn:
        if input("Bitte geben Sie die Geheimzahl ein: ") == pin:
            loggedIn = True
            while loggedIn:
                choice = menu()
                if choice == 3:
                    break
                elif choice == 2:
                    bal = withdraw(bal)
                elif choice == 1:
                    checkbal()
        else:
            attempts += 1
            if attempts == 3:
                print("Ihr Konto wurde gesperrt!")
                break

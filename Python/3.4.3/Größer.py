a = int(input("Zahl 1: "))
b = int(input("Zahl 2: "))
c = int(input("Zahl 3: "))

# TODO: Optimieren

if a >= b:
    if a >= c:
        if c >= a:
            if b >= c:
                print("A, B und C sind gleich groß")
                exit()
            print("A und C sind gleich groß")
            exit()
    if b >= c:
        if b >= a:
            if a >= b:
                print("A und B sind gleich groß")
                exit()
            print("B ist am größten")
            exit()
        print("A ist am größten")
        exit()
    if c >= b:
        if c >= a:
            print("C ist am größten")
            exit()
        print("B ist am größten")
        exit()
    print("A ist am größten")
    exit()
elif b >= a:
    if c >= b:
        if b >= c:
            print("B und C sind gleich groß")
            exit()
        print("C ist am größten")
        exit()
    print("B ist am größten")
    exit()

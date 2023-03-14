def date():
    for y in range(1901, 2001):
        for m in range(1, 13):
            for d in range(1, 31):
                if d <= 29 and m == 2 and y % 4 == 0:
                    valid_date = True
                elif d <= 30 and m in [4, 6, 9, 11]:
                    valid_date = True
                else:
                    valid_date = True

                if valid_date:
                    if d * m == int(str(y)[2:len(str(y))]):
                        print("Magisches Datum:", y, m, d)


date()

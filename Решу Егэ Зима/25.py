for n in range(400000000,600000000):
    for m in range(0, 100000000, 2):
        for n in range(1, 10000000, 2):
            d = (2**m) * (3 ** n)
            if n == d:
                print(n)

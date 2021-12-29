from decimal import Decimal

Y = 0
while Y == 0:
    cont, l1 = 0, 0
    while cont<2:
        X = float(input())
        if X >= 0 and X <= 10:
            l1 += X
            cont +=1
        else:
            print("nota invalida")
            continue
    media = Decimal((l1/2))
    print("media = %.2f" % media)
    while True:
        print("novo calculo (1-sim 2-nao)")
        n = input()
        if '2' in n:
            Y = 1
            break
        elif '1' in n:
            Y = 0
            break
        else:
            continue
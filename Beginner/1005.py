from decimal import *
A = float(input())
B = float(input())

if (A >=0 and A <=10) and (B >=0 and B <=10):
    MEDIA = Decimal(((A*3.5) + (B*7.5))/11)
    print("MEDIA =", round(MEDIA, 5))
else:
    print('entrada invalida')

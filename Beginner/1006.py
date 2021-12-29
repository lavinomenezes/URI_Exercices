from decimal import *
A = float(input())
B = float(input())
C = float(input())

if (A >=0 and A <=10) and (B >=0 and B <=10) and (C >=0 and C <=10):
    MEDIA = Decimal((A*.2) + (B*.3)+(C*.5))
    print("MEDIA =", round(MEDIA, 1))
else:
    print('entrada invalida')

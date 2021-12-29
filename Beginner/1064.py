from decimal import *
X = 0
Y = 0
TOTAL = 0
while X < 6:
    V = float(input())
    if V>0:
        Y += 1
        TOTAL += V
    X += 1
MEDIA = Decimal(TOTAL/4)
print(Y, "valores positivos")
print(round(MEDIA,1))

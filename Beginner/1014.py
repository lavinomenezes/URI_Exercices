from decimal import *
X = int(input())
Y = float(input())
CON = Decimal(X/Y)
print(round(CON,3), "km/l")
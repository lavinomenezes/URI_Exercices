from decimal import *
X = input().split()
Y = input().split()
TOTAL = int(X[1])*float(X[2])+int(Y[1])*float(Y[2])
TOTAL = Decimal(TOTAL)
print("VALOR A PAGAR: R$", round(TOTAL,2))


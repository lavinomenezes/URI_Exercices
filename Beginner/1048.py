from decimal import *
X = float(input())
if X >= 0 and  X <= 400:
    Y = X + (X*0.15)
if X > 400 and  X <= 800:
    Y = X + (X*0.12)
if X > 800 and  X <= 1200:
    Y = X + (X*0.10)
if X > 1200 and  X <= 2000:
    Y = X + (X*0.07)
if X > 2000:
    Y = X + (X*0.04)
porc = Decimal(((Y-X)/X)*100) if X != 0 else 15
print("Novo salario: %.2f" % Decimal(Y))
print("Reajuste ganho: %.2f" % Decimal(float(Y-X)))
print("Em percentual:",round(porc,0) , "%")



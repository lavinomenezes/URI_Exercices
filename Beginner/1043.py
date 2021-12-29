from decimal import *
valores = list()
X = input().split()
for n in X:
    valores.append(float(n))
valores.sort()
if (valores[0]+valores[1]) <= valores[2]:
    area = Decimal(((valores[1]+valores[2])*valores[0])/2)
    print("Area =", round(area,1))
else:
    peri = Decimal(valores[0] + valores[1] + valores[2])
    print("Perimetro =", round(peri,1))

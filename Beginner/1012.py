from decimal import *
X = input().split()
A = float(X[0])
B = float(X[1])
C = float(X[2])
pi = 3.14159
TRIANGULO = Decimal((A*C)/2)
CIRCULO = Decimal(pi*C**2)
TRAPEZIO = Decimal(((A+B)*C)/2)
QUADRADO = Decimal(B**2)
RETANGULO = Decimal(A*B)
print("TRIANGULO:", round(TRIANGULO, 3))
print("CIRCULO:", round(CIRCULO, 3))
print("TRAPEZIO:", round(TRAPEZIO, 3))
print("QUADRADO:", round(QUADRADO, 3))
print("RETANGULO:", round(RETANGULO, 3))


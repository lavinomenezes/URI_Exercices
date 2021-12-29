from math import sqrt
from decimal import *
X = input().split()
A = float(X[0])
B = float(X[1])
C = float(X[2])
DELTA = (B**2 - (4*A*C))
if DELTA >= 0 and A != 0:
    R1 = Decimal(((-B) + sqrt(DELTA))/(2*A))
    R2 = Decimal(((-B) - sqrt(DELTA))/(2*A))
    print("R1 =", round(R1, 5))
    print("R2 =", round(R2, 5))
else:
    print("Impossivel calcular")
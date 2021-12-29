import math
from decimal import *
X = input().split()
Y = input().split()
X1 = float(X[0])
X2 = float(Y[0])
Y1 = float(X[1])
Y2 = float(Y[1])

DIS = Decimal(math.sqrt(((X2-X1)**2)+((Y2-Y1)**2)))

print(round(DIS, 4))

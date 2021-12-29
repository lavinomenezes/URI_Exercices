from decimal import *
N = int(input())
for i in range(0,N):
    X = input().split()
    A = float(X[0])
    B = float(X[1])
    C = float(X[2])
    media = Decimal((A*0.2)+(B*0.3)+(C*0.5))
    print("%.1f" % media)
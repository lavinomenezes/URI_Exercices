def soma(*args):
    X = 0
    for i in args:
        X += i
    return X

from decimal import Decimal
D = 0
div = 0
s = 0
l1 = list()
aux = list()
op = str(input())
for i in range(0,12):
    for j in range(0,12):
        X = float(input())
        aux.append(X)
    l1.append(aux[:])
    aux.clear()
for i in range(0,len(l1)):
    div += i
if 'S' in op:
    D = len(l1)
    for i in l1:
        s += soma(*i[D:len(i)])
        D -= 1
    print("%.1f" % s)
elif 'M' in op:
    D = len(l1)
    for i in l1:
        s += soma(*i[D:len(i)])
        D -= 1
    m = Decimal(s/div)
    print("%.1f" % m)
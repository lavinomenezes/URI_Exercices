from decimal import Decimal
l1 = list()
aux = list()
op = input()
for i in range(12):
    for j in range(12):
        X = float(input())
        aux.append(X)
    l1.append(aux[:])
    aux.clear()
D = 1
F, div = len(l1), len(l1)
s, tam = 0, 0
if 'S' in op:
    for i in range(0,int(len(l1)/2)):
        s += sum(l1[i][D:F-1])
        D += 1
        F -= 1
    print("%.1f" % s)
elif 'M' in op:
    for i in range(0,int(len(l1)/2)):
        s += sum(l1[i][D:F-1])
        D += 1
        F -= 1
        div -=2
        tam += div
        m = Decimal(s/tam)
    print("%.1f" % m)
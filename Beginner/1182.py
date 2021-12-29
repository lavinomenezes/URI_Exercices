from decimal import Decimal
s = 0
l1 = list()
aux = list()
C = int(input())
op = str(input())
for i in range(0,12):
    for j in range(0,12):
        X = float(input())
        aux.append(X)
    l1.append(aux[:])
    aux.clear()

if 'S' in op:
    for i in l1:
        for j in range(0,len(l1)):
            if j == C:
                s += i[j]
    print("%.1f" % s)
elif 'M' in op:
    for i in l1:
        for j in range(0,len(l1)):
            if j == C:
                s += i[j]
    media = Decimal(s/len(l1))
    print("%.1f" % media)
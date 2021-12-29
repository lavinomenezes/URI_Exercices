def soma(*args):
    X = 0
    for i in args:
        X += i
    return X
def media(*args):
    from decimal import Decimal
    X = 0
    for i in args:
        X += i
    return Decimal(X/len(args))


l1 = list()
aux = list()
linha = int(input())
op = str(input())
for i in range(0,12):
    for j in range(0,12):
        X = float(input())
        aux.append(X)
    l1.append(aux[:])
    aux.clear()

if 'S' in op:
    s = soma(*l1[linha])
    print("%.1f" % s)
elif 'M' in op:
    m = media(*l1[linha])
    print("%.1f" % m)
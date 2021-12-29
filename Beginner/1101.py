lista = list()
Y = 0
while True:
    soma = 0
    lista.clear()
    X = input().split()
    for i in range(0, len(X)):
        lista.append(int(X[i]))
    lista.sort()
    if lista[0] == lista[1] and (lista[0] > 0 and lista[1] > 0):
        print("0 Sum=0")
    elif lista[0] > 0 and lista[1] > 0:
        for i in range(lista[0], lista[1]+1):
            print(str(i) + " ", end= '')
            soma += i
        print("Sum=%.0f" % soma)
    else:
        break

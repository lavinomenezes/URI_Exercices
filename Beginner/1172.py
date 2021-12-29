lista = list()
for i in range(0,10):
    X = int(input())
    lista.append(X)
for i, c in enumerate(lista):
    if c <= 0:
        c = 1
        print("X[" + str(i) + "]" + " = " + str(c))
    else:
        print("X[" + str(i) + "]" + " = "  + str(c))
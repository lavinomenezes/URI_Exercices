lista = list()
for i in range(0,100):
    X = float(input())
    lista.append(X)
for i, c in enumerate(lista):
    if c <= 10:
        print("A[" +str(i) + "]" + " = " + str(c))
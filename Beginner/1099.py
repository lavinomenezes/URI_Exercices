lista = list()
lista2 = list()
X = int(input())
for i in range(0, X):
    lista2.clear()
    impar = 0
    extr = input().split()
    for i in range(0, len(extr)):
        lista2.append(int(extr[i]))
    lista2.sort()
    Y = lista2[0]
    Z = lista2[1]
    for i in range(Y+1,Z):
        if i%2 != 0:
            impar += i
    lista.append(impar)
for i in lista:
    print(i)
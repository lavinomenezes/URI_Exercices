lista = list()
maior = 0
pos = 0
for i in range(0,100):
    X = int(input())
    if X > maior:
        maior = X
        pos = i
    lista.append(X)
print(maior)
print(pos+1)

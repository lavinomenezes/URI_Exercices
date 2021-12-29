X = 0
PA = 0
I = 0
N = 0
PO = 0
while X < 5:
    V = int(input())
    if V % 2 == 0:
        PA += 1
        if V > 0:
            PO += 1
        elif V < 0:
            N += 1
    elif V % 2 != 0:
        I += 1
        if V > 0:
            PO += 1
        elif V < 0:
            N += 1
    X += 1
print(PA, "valor(es) par(es)")
print(I, "valor(es) impar(es)")
print(PO, "valor(es) positivo(s)")
print(N, "valor(es) negativo(s)")
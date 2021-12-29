X = int(input())
l1 = []
cont = 0
test = 1
while cont < X:
    Y = int(input())
    l1.append(Y)
    cont +=1
cont = 0
while cont < len(l1):
    test = 1
    perf = 0
    Z = l1[cont]
    while test < Z:
            if Z%test == 0:
                perf += test
            test +=1
    if perf == Z:
        print(Z, "eh perfeito")
    else:
        print(Z, "nao eh perfeito")
    cont +=1
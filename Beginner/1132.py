X = int(input())
Y = int(input())
soma = 0
if X < Y:
    for i in range(X,Y+1):
        if i % 13 == 0:
            continue
        else:
            soma += i
    print(soma)
else:
    for i in range(X,Y-1,-1):
        if i%13 == 0:
            continue
        else:
            soma += i
    print(soma)
for i in range(int(input())):
    X = int(input())
    veri = 0
    for i in range(X+1,0,-1):
        if X%i == 0:
            veri+=1
    if veri == 2:
        print(X,"eh primo")
    else:
        print(X,"nao eh primo")
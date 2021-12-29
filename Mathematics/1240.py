for i in range(int(input())):
    X, Y = input().split()
    n = len(Y)
    if X[-n:] == Y:
        print("encaixa")
    else:
        print("nao encaixa")
while True:
    X = input().split()
    Y = int(X[0])
    Z = int(X[1])
    if Y == Z:
        break
    else:
        if Y > Z:
            print("Decrescente")
        else:
            print("Crescente")

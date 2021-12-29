while True:
    try:
        X, Y = map(int,input().split())
    except EOFError:
        break
    print(abs(X-Y))
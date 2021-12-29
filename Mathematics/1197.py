while True:

    try:
        X, Y = map(int,input().split())
    except EOFError:
        break
    print((Y*2)*X)
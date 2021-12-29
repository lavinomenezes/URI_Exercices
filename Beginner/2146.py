while True:
    try:
        X = int(input())
    except EOFError:
        break
    print(X-1)
while True:
    f = ''
    X, Y = map(int,input().split())
    if X == 0 and Y == 0:
        break
    s = str(X+Y)
    for i in s:
        if i != '0':
            f += i
    print(f)
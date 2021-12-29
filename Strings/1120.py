while True:
    X, Y = input().split()
    if X == '0' and Y == '0':
        break
    errado = ''
    for i in Y:
        if i != X:
            errado+=i
    if len(errado)==0:
        print(0)
    else:
            print(int(errado))
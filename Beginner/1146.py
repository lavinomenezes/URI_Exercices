while True:
    X = int(input())
    if X == 0:
        break
    else:
        for i in range(0,X):
            if i < X-1:
                print(i+1, end=' ')
            elif i == X-1:
                print(i+1, end='')
                print()
        continue
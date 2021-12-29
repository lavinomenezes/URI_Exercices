while True:
    try:
        l1 = list()
        x, y = map(int,input().split())
        for i in range(x):
            l1.append(int(input()))
        l1.sort(reverse=True)
        for i in range(y):
            k = int(input())
            print(l1[k-1])
    except EOFError:
        break
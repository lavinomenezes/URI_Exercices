X, Y = map(int,input().split())
l1 = [int(x) for x in input().split()]
for i in range(X):
    e = int(input())
    if e in l1:
        print(0)
    else:
        print(1)
        l1.append(e)
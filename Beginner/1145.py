X, Y = map(int,input().split())
count = 1
Z = 0
for i in range(1,Y+1):
    if count < X:
        print("%.0f" % i, end=' ')
        count += 1
    elif count == X:
        print("%.0f" % i, end='')
        print()
        count = 1
    if i == Y+1:
        print(' ')
x = 1
while True:
    a, b = 0, 0
    x = int(input())
    if x == 0:
        break
    for i in range(x):
        y, z = map(int,input().split())
        if y>z:
            a+=1
        elif z>y:
            b +=1
    print(a,b)
X, Y, Z = map(int,input().split())
s = X + Y + Z
if s == 24:
    print(0)
else:
    if s > 24:
        s = s -24
        print(s)
    elif s < 0:
        s = s + 24
        print(s)
    else:
        print(s)
for _ in range(int(input())):
    x, y = map(int,input().split())
    txt = ''
    for i in range(x,y+1):
        txt += str(i)
    n = "".join(txt+"".join(reversed(txt)))
    print(n)
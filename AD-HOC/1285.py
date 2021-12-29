while True:
    try:
        x, y = map(int,input().split())
    except EOFError:
        break
    d = 0
#O(n)
    for i in range(x,y+1):
        s = set(str(i))
        if len(str(i)) == len(s):
            d+=1

    print(d)


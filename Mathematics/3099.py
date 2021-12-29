while True:
    y = int(input())
    x = int(input())
    txt = ''
    for i in range(y,x+1):
        txt += str(i)
    w = txt.count("1")
    z = txt.count("7")
    print(w+z)
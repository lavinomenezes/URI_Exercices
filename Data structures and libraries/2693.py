while True:
    try:
        aux = list()
        l1 = list()
        for i in range(int(input())):
            txt = input().split()
            l1.append([txt[0],txt[1],int(txt[2])])
        l1.sort(key=lambda x:(x[2],ord(x[1]),x[2]))
        for _ in l1:
            print(_[0])
    except EOFError:
        break
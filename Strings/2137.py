while True:
    try:
        l1 = list()
        for i in range(int(input())):
            l1.append(input())
        l1.sort()
        for _ in l1:
            print(_)
    except EOFError:
        break
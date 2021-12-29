while True:
    try:
        txt = input()
        x = int(input())
        l1 = [int(x) for x in input().split()]
        for i in range(x):
            if i != x-1:
                print(txt[l1[i]-1],end='')
            else:
                print(txt[l1[i]-1])

    except EOFError:
        break
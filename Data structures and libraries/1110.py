while True:
    n = int(input())
    if n == 0:
        break
    l1 = [x for x in range(1,n+1)]
    l2 = list()
    while len(l1)>=2:
        l2.append(str(l1[0]))
        l1.pop(0)
        l1.append(l1[0])
        l1.pop(0)
    print("Discarded cards:", ", ".join(l2))
    print("Remaining card:", *l1)


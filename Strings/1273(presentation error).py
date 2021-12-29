while True:
    x = int(input())
    if x == 0:
        break
    l1 = list()
    for j in range(x):
        l1.append(input())
    just = 0
    for _ in l1:
        if len(_) > just:
            just = len(_)
    for i in l1:
        print(i.rjust(just))
    print()
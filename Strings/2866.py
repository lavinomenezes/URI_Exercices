for i in range(int(input())):
    txt = input()
    l1 = "".join(reversed([x for x in txt if x.islower()]))
    print(l1)


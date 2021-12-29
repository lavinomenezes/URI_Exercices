from itertools import zip_longest
for _ in range(int(input())):
    prim = input()
    seg = input()
    l1 = [prim[i:i+2] for i in range(0,len(prim),2)]
    l2 = [seg[i:i+2] for i in range(0,len(prim),2)]
    txt = zip_longest(l1,l2,fillvalue='')
    for j in txt:
        for v in j:
            print(v, end='')
    print()
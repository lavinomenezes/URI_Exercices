"""""rep = 0
X = int(input())
while rep<X:
    count, pos = 0, 0
    pri, seg = map(str,input().split())
    new = ''
    if len(pri) > len(seg):
        while count<len(seg):
            new += pri[pos]
            new += seg[pos]
            pos+=1
            count+=1
        new += pri[pos:len(pri)]
    elif len(pri) < len(seg):
        while count<len(pri):
            new += pri[pos]
            new += seg[pos]
            pos+=1
            count+=1
        new += seg[pos:len(seg)]
    elif len(pri) == len(seg):
        while count < len(pri):
            new += pri[pos]
            new += seg[pos]
            pos += 1
            count += 1
    rep+=1
    print(new)
"""""
from itertools import zip_longest
count = 0
X = int(input())
while count < X:
    prim, seng = input().split()
    txt = zip_longest(prim,seng, fillvalue='')
    for i in txt:
        for j in i:
            print(j, end='')
    print()
    count += 1

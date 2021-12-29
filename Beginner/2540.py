from collections import Counter
while True:
    try:
        X = int(input())
        l1 = list(map(int,input().split()))
    except EOFError:
        break
    d1 = Counter(l1)
    if d1[1] >= ((2/3)*len(l1)):
        print("impeachment")
    else:
        print("acusacao arquivada")


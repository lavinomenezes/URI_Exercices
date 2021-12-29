from collections import Counter
for i in range(int(input())):
    l1 = list()
    for i in range(int(input())):
        l1.append(input())
    d1 = Counter(l1)
    if len(d1) > 1:
        print("ingles")
    else:
        print(l1[0])
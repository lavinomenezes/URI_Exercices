from collections import Counter
for i in range(int(input())):
    X = int(input())
    l1 = [x for x in input().split()]
    l2 = [x for x in input().split()]
    for i in range(len(l1)):
        d1 = Counter(l2[i])
        if d1['P']<((d1['P']+d1['A'])*0.75):
            print(l1[i],end='')
            if i != len(l1) - 1:
                print(" ", end='')
    print()

"""n = int(input())

while (n > 0):
    n -= 1
    a = int(input())
    l = input().split()
    p = input().split()
    for ind, a in enumerate(p):
        a = a.replace('M', '')
        old = len(a)
        a = a.replace('A', '')
        new = len(a)
        try:
            new /= old
            if (new >= 0.75):
                l[ind] = '-'
        except ZeroDivisionError:
            l[ind] = '-'

    l = [a for a in l if a is not '-']
    for ind, a in enumerate(l):
        print(a, end='')
        if (ind != len(l) - 1):
            print(' ', end='')
    print()"""
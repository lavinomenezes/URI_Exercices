from statistics import median
for i in range(int(input())):
    l1 = [int(x) for x in input().split()]
    for j in l1:
        if j < 11 or j >20:
            l1.remove(j)
    print("Case " + str(i+1)+":", median(l1))
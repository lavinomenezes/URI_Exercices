l1 = list()
for i in range(int(input())):
    l1.append(int(input()))
l2 = [x for x in l1 if x%2==0]
l3 = [x for x in l1 if x%2!=0]
l4 = sorted(l2) + sorted(l3,reverse=True)
for j in l4:
    print(j)


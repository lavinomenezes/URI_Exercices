from collections import Counter
X = int(input())
l1 = [int(x) for x in input().split()]
d1 = Counter(l1)
print(d1[X])
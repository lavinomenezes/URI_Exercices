from collections import Counter
X = input()
d1 = Counter(X)
if d1['1']%2 == 0:
    print(X+'0')
else:
    print(X+'1')
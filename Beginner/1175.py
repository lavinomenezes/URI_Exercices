N = list()
for i in range(0,20):
    X = int(input())
    N.insert(0, X)
for i, c in enumerate(N):
    print("N[" + str(i) + "]" + " = " + str(c))

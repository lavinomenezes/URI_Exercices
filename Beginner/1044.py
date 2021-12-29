V = list()
X = input().split()
for n in X:
    V.append(int(n))
V.sort()
if V[1]%V[0] == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")

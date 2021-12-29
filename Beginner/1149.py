s = 0
aux = [int(x) for x in input().split() if x>'0']
for i in range(0,aux[1]):
    s += aux[0]+i
print(s)
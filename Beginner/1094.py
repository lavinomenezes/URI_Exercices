from decimal import *
X = int(input())
R = 0
S = 0
C = 0
total = 0
for i in range(0,X):
    ent = input().split()
    Q = int(ent[0])
    T = str(ent[1])
    if T in 'Cc':
        C += Q
        total += Q
    elif T in 'Rr':
        R += Q
        total +=Q
    else:
        S += Q
        total+=Q
print("Total:", total, "cobaias")
print("Total de coelhos:", C)
print("Total de ratos:", R)
print("Total de sapos:", S)
print("Percentual de coelhos: %.2f" % float(Decimal(C*(100/total))), "%")
print("Percentual de ratos: %.2f" % float(Decimal(R*(100/total))), "%")
print("Percentual de sapos: %.2f" % float(Decimal(S*(100/total))), "%")
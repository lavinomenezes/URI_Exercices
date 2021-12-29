X = input().split()
A = int(X[0])
B = int(X[1])
C = int(X[2])

MAIOR = int((A+B+abs(A-B))/2)

if MAIOR > C:
    print(MAIOR, "eh o maior")
else:
    print(C, "eh o maior")

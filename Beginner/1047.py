X = input().split()
A = int(X[0])
B = int(X[1])
C = int(X[2])
D = int(X[3])
hora1 = 0
hora2 = 0
min1 = 0
min2 = 0
if A == B == C == D or ((A == C) and (B == D)):
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
elif A == C:
    if B > D:
        for i in range(B, 60):
            min1 += 1
        for i in range(0, D):
            min2 += 1
        if min1 + min2 >= 60:
            mint = (min1 + min2) - 60
        else:
            mint = min1 + min2
        print("O JOGO DUROU 23 HORA(S) E", mint, "MINUTO(S)")
    else:
        for i in range(B,60):
            min1 += 1
        for i in range(0,D):
            min2 += 1
        if min1+min2 >= 60:
            mint = (min1+min2) - 60
        else:
            mint = min1 + min2
        print("O JOGO DUROU 0 HORA(S) E", mint, "MINUTO(S)")

elif C > A:
    hotaf = C - A
    for i in range(B,60):
        min1 += 1
    for i in range(0,D):
        min2 += 1
    if min1+min2 >= 60:
        mint = (min1+min2) - 60
        hora1 +=1
    else:
        mint = min1 + min2

    hotaf = 0 if hotaf == 1 and (min2+min1)<60 and(B<D) else C-A
    if B > D:
        hotaf = hotaf -1
    print("O JOGO DUROU", hotaf, "HORA(S) E",mint,"MINUTO(S)")
else:
    for i in range(A,24):
        hora1 +=1
    for i in range(0,C):
        hora2 += 1
    for i in range(B,60):
        min1 += 1
    for i in range(0,D):
        min2 += 1
    if min1+min2 >= 60:
        mint = (min1 + min2) - 60
    else:
        mint = min1 + min2
    if B > D:
        hotaf =  (hora1+hora2) -  1
    else:
        hotaf = (hora1 + hora2)
    print("O JOGO DUROU", hotaf, "HORA(S) E",mint,"MINUTO(S)")
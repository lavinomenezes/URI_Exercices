X = input().split()
A = int(X[0])
B = int(X[1])
cont =0
cont2 =0
if A == B:
    print("O JOGO DUROU 24 HORA(S)")
elif B > A:
    dur = B - A
    print("O JOGO DUROU", dur, "HORA(S)")
else:
    for i in range(A,24):
        cont += 1
    for i in range(0,B):
        cont2 +=1
    print("O JOGO DUROU", (cont+cont2), "HORA(S)")

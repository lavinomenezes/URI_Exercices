I = 0
G = 0
GRENAL = 0
count = 0
impt = 0
while count == 0:
    X, Y = map(int,input().split())
    if X > Y:
        I += 1
    elif X < Y:
        G += 1
    elif X == Y:
        impt += 1
    GRENAL += 1
    while True:
        n = input("Novo grenal (1-sim 2-nao)\n")
        if '1' in n:
            count = 0
            break
        elif '2' in n:
            count = 1
            break
        else:
            continue
print(GRENAL, "grenais")
print("Inter:%.0f" % I)
print("Gremio:%.0f"% G)
print("Empates:%.0f"% impt)
if I>G:
    print("Inter venceu mais")
elif G>I:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")
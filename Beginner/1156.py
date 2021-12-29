cima,baixo = 1, 1
S = 0
while True:
    S += cima/baixo
    cima+=2
    baixo*=2
    if cima == 39:
        break
print("%.2f" % S)

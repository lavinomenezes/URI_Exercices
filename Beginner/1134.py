X, al, gas, dis = 0, 0, 0, 0
while X == 0:
    Y = int(input())
    if Y == 1:
        al += 1
    elif Y == 2:
        gas += 1
    elif Y == 3:
        dis += 1
    else:
        if Y == 4:
            X = 1
            break
        else:
            x = 0
            continue
print("MUITO OBRIGADO")
print("Alcool:", al)
print("Gasolina:", gas)
print("Diesel:", dis)
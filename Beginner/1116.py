for i in range(int(input())):
    Y, Z = map(float, input().split())
    if Z == 0:
        print("divisao impossivel")
    else:
        print(format(Y/Z, ".1f"))


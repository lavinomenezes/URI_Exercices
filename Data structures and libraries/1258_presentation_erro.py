while True:
    aux = list()
    alunos = list()
    _ = int(input())
    if _ == 0:
        break
    for i in range(_):
        aux.append(input())
        x, y = input().split()
        aux.append(x)
        aux.append(y)
        alunos.append(aux[:])
        aux.clear()
    alunos.sort(key=lambda z:(z[1],-(ord(z[2])),z[0]))
    for i in alunos:
        print(i[1],i[2],i[0])
    print("\n")


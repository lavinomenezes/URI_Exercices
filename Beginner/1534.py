while True:
    try:
        x = int(input())
        l1 = list()
        aux = list()
        count = 0
        cont = x-1
        for i in range(x):
            for j in range(x):
                if j == cont:
                    aux.append(str(2))
                elif j == count:
                    aux.append(str(1))
                else:
                    aux.append(str(3))
            count +=1
            cont -=1
            l1.append(aux[:])
            aux.clear()

        for i in l1:
            print("".join(i))
    except EOFError:
        break
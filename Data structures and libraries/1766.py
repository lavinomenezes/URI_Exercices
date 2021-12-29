for i in range(int(input())):
    a, b = (map(int,input().split()))
    l1 = list()
    aux = list()
    for j in range(a):
        aux = input().split()
        l1.append([aux[0],int(aux[1]),int(aux[2]),float(aux[3])])

    l1.sort(key=lambda x:(-x[1],x[2],x[3],x[0]))
    print("CENARIO {" + str(i+1) + "}")
    for v in range(b):
        print(str(v+1) + " - " + str(l1[v][0]))

"""
Rudolph 50 100 1.12
Dasher 10 121 1.98
Dancer 10 131 1.14
Prancer 7 142 1.36
Vixen 50 110 1.42
Comet 50 121 1.21
Cupid 50 107 1.45
Donner 30 106 1.23
Blitzen 50 180 1.84
"""
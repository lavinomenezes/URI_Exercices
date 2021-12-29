def pesquisa_binaria(lista,valor):
    lim_inf = 0
    lim_sup = len(lista)-1
    while lim_inf <= lim_sup:
        pos_atual = (lim_inf+lim_sup)//2
        if lista[pos_atual] > valor:
            lim_sup = pos_atual-1
        elif lista[pos_atual] < valor:
            lim_inf = pos_atual+1
        else:
            if lista[pos_atual] == valor and lista[pos_atual - 1] != valor or pos_atual - 1 < 0:
                return pos_atual
            lim_sup = pos_atual -1
    return -1

def particao(vetor,inicio,final):
    pivo = vetor[final]
    i = inicio -1

    for j in range(inicio,final):
        if vetor[j] <= pivo:
            i += 1
            vetor[i], vetor[j] = vetor[j], vetor[i]
    vetor[i+1], vetor[final] = vetor[final], vetor[i+1]
    return i+1

def quick_sort(vetor,inicio,final):
    if inicio < final:
        pos = particao(vetor,inicio,final)
        #esquerda
        quick_sort(vetor,inicio, pos-1)
        #direita
        quick_sort(vetor, pos+1,final)
    return vetor

"""
Provavelmente a ordenação está demorando muito, quando aprender outros metodos volto
"""
count = 0
while True:
    count +=1
    l1 = list()
    x, y = (map(int,input().split()))
    if x == 0 and y == 0:
        break
    for i in range(x):
        l1.append(int(input()))
    l1 = quick_sort(l1,0,len(l1)-1)
    print("CASE# " + str(count) + ':')
    for v in range(y):
        p = int(input())
        a = pesquisa_binaria(l1,p)
        if a == -1:
            print(p, "not found")
        else:
            print(p,"found at", a+1)


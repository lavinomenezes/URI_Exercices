from collections import Counter
i = 0
while True:
    try:
        txt = input()
    except EOFError:
        break
    l1 = list()
    d1 = Counter(txt)
    for c,v in d1.items():
        l1.append([ord(c),v])
    l1.sort(key=lambda x:(x[1],-x[0]))
    """"
    Isso gera uam tupla con tendo x[1] segundo elemento que vai primeiro por ser prioridade, -x[0] o primeiro elemento que é negativo para ser em 
    ordem descrescente
    quando a ordenação é feita dessa forma A ORDENAÇÃO É FEITA COM BASE NO PRIMEIRO ELEMENTO (X,0) E CASO SEJEM IGUAIS É FEITO COM BASE NO SEGUNDO (0,X)
    """
    if i != 0:
        print()
    for c, v in l1:
        print(c, v)
    i += 1

"""l1.sort(key=lambda x:x[1])
print(l1,1)
for i in range(len(l1)):
    if i == 0:
        aux.append([l1[i]])
    else:
        if aux[-1][0][1]==l1[i][1]:
            aux[-1].append(l1[i])
        else:
            aux.append([l1[i]])
for i in aux:
    i.sort(key=lambda y:y[0],reverse=True)
    print(i)"""


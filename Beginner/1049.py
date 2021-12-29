lista = list()
for i in range(0,3):
    X = str(input())
    lista.append(X)
if lista[0] == 'vertebrado':
    if lista[1] == 'ave':
        if lista[2] == 'carnivoro':
            print("aguia")
        else:
            print("pomba")
    else:
        if lista[2] == 'onivoro':
            print("homem")
        else:
            print("vaca")
else:
    if lista[1] == 'inseto':
        if lista[2] == 'hematofago':
            print("pulga")
        else:
            print("lagarta")
    else:
        if lista[2] == 'hematofago':
            print("sanguessuga")
        else:
            print("minhoca")
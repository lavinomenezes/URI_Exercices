DDD = [[61,'Brasilia'],[71,'Salvador'],[11,'Sao Paulo'],[21, 'Rio de Janeiro'],
       [32,'Juiz de Fora'],[19,'Campinas'],[27,'Vitoria'],[31,'Belo Horizonte']]
X = int(input())
for i in range(0,len(DDD)):
    if DDD[i][0] == X:
        print(DDD[i][1])
        break
    elif i >= len(DDD)-1:
        print("DDD nao cadastrado")
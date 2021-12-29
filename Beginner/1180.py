X = int(input())
Y = input().split()
menor = min(map(int,Y))
print("Menor valor:",menor)
print("Posicao:", Y.index(str(menor)))


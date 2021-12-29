from decimal import Decimal
l1 = list()
cont = 0
while cont<2:
    X = float(input())
    if X >= 0 and X <=10:
        l1.append(X)
        cont +=1
    else:
        print("nota invalida")
        continue
media = Decimal((l1[0]+l1[1])/2)
print("media =", round(media,2))
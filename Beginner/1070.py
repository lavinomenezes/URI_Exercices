X = int(input())
count = 0
impar = X
while count < 6:
    if impar%2 != 0:
        print(impar)
        count += 1
        impar += 1
    else:
        impar += 1
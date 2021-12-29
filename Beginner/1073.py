X = int(input())
count = 0
for i in range(0,X+1):
    if i%2 == 0 and i > 0:
        print(i,end='')
        print("^2 =", i**2)


X = int(input())
for i in range(1,X+1):
    count = 1
    for j in range(0,3):
        if j <2:
            print(i**count, end=' ')
            count += 1
        else:
            print(i**count, end='')
            count+=1
    print()


X = int(input())
for i in range(1,X+1):
    for j in range(0,2):
        print(str(i)+ " "+ str((i**2)+j)+ " " + str((i**3)+j))
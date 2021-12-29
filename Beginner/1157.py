X = int(input())
n1 = [i for i in range(1,X+1) if X%i==0]
for i in n1:
    print(i)
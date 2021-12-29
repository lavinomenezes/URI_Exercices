X = int(input())
l1 = list(map(int,input().split()))
for i in range(1,len(l1)):
    if l1[i] < l1[i-1]:
        print(i+1)
        break
    elif i == len(l1)-1:
        print(0)

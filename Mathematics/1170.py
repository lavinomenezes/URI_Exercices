
for i in range(int(input())):
    count = 0
    X = float(input())
    while X>1:
        X = X/2
        count+=1
    print(count,"dias")

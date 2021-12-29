X = int(input())
Y = 1
if X >= 1 and X <= 1000:
    while Y <= X:
        if Y%2 != 0:
            print(Y)
        Y +=1

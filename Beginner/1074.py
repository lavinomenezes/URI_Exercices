X = int(input())
for i in range(0,X):
    Y = int(input())
    if Y > 0:
        if Y%2 == 0:
            print("EVEN POSITIVE")
        else:
            print("ODD POSITIVE")
    elif Y < 0:
        if Y%2 == 0:
            print("EVEN NEGATIVE")
        else:
            print("ODD NEGATIVE")
    else:
        print("NULL")
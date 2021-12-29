def fatorial(X):
    count = 1
    for i in range(X,0,-1):
        count *= i
    return count

while True:
    try:
        X,Y = map(int,input().split())
    except EOFError:
        break
    print(fatorial(X)+fatorial(Y))
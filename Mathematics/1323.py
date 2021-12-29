while True:
    x = int(input())
    if x == 0:
        break
    n = (x*((x+1)*(2*x+1)))/6
    print(int(n))
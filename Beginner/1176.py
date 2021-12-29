def fibonaci(X):
    fib = [0,1]
    for i in range(0,X):
        som = fib[-1] + fib[-2]
        fib.append(som)
    return fib
Y = int(input())
for i in range(0,Y):
    X = int(input())
    fib = fibonaci(X)
    print("Fib(" + str(X) +")" + " = " + str(fib[X]))

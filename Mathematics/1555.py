def r(X,Y):
    resultado = (3*X)**2 + Y**2
    return resultado
def b(X,Y):
    resultado = 2*(X**2) +(5*Y)**2
    return resultado
def c(X,Y):
    resultado = -100*X + (Y**3)
    return resultado
rep = int(input())
for i in range(0,rep):
    arg = input().split()
    X = int(arg[0])
    Y = int(arg[1])
    if r(X,Y) > b(X,Y) and r(X,Y) > c(X,Y):
        print("Rafael ganhou")
    elif b(X,Y) > r(X,Y) and b(X,Y) > c(X,Y):
        print("Beto ganhou")
    elif c(X,Y) > r(X,Y) and c(X,Y) > b(X,Y):
        print("Carlos ganhou")
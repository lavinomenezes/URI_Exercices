from math import sqrt, pi
while True:
    try:
        x,y,z = map(int,input().split())
    except EOFError:
        break
    p = (x+y+z)/2
    at = sqrt(p*(p-x)*(p-y)*(p-z))
    As = (((x*y*z)/(4*at))**2)*pi - at
    r = at/p
    Ar = (r**2)*pi
    Av = at - Ar
    print("%.4f" % As, end=' ')
    print("%.4f" % Av, end=' ')
    print("%.4f" % Ar)
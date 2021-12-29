from math import trunc
while True:
    x, y, z = map(int,input().split())
    if x == 0 and y == 0 and z == 0:
        break
    v = trunc((x*y*z)**(1/3))
    print(v)
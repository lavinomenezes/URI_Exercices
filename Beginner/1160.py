from math import floor
soma = 0
for i in range(int(input())):
    pa, pb, g1, g2 = map(float, input().split(" "))
    soma = pa
    for i in range(1,102):
        pa += floor(int(pa)*(g1/100))
        #pb += floor(int(pb)*(g2/100))
        X = floor(soma*((1+g1/100)**i))
        print(i, pa, X)




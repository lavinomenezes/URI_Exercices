from math import ceil
I = 0
J = 1
while I <=2:
    for i in range(0,3):
        if (I == 0 ) or (I >= 1.9999) or (I == 1):
            print("I=%.0f" % int(ceil(I)), end='')
            print(" J=%.0f" % int(J))
        else:
            print("I=%.1f" % round(I, 1), end='')
            print(" J=%.1f" % round(J, 1))
        J += 1
    J = J - 3
    J += 0.2
    I += 0.2
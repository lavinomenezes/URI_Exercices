for i in range(int(input())):
    x = int(input())
    t1 = [int(x) for x in input().split()]
    t2 = [int(x) for x in input().split()]
    vg1 = (t1[0]+t1[1])/2
    if t1[2]%2 == 0:
        vg1 = vg1 + x
    vg2 = (t2[0] + t2[1]) / 2
    if t2[2]%2 == 0:
        vg2 = vg2 + x
    if vg1>vg2:
        print('Dabriel')
    elif vg1==vg2:
        print("Empate")
    else:
        print("Guarte")
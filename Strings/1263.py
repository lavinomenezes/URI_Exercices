while True:
    try:
        txt = input()
    except EOFError:
        break

    count = 0
    l2 = [x[0].lower() for x in txt.split()]
    l3 = list()
    for i in range(len(l2)):
        if i == 0:
            l3.append([l2[i]])
        else:
            if l2[i] == l2[i-1]:
                l3[len(l3)-1].append(l2[i])
            else:
                l3.append([l2[i]])
    for i in l3:
        if len(i)>1:
            count+=1
    print(count)

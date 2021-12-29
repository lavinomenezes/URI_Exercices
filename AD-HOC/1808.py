aux = input()
l1 = list()
if len(aux) == 1:
    l1.append(int(aux))
else:
    tam = iter(range(0,len(aux)))
    for i in tam:
        if aux[i] == '1' and aux[i+1] == '0':
            l1.append(int(aux[i]+aux[i+1]))
            i = next(tam)
        else:
            l1.append(int(aux[i]))
s = sum(l1)/len(l1)
print("%.2f" % s)
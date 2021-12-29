txt = 'cbufllatkz'
l1 = ['cbofllafkz', 'cbhflluteq','cbuzqzatmz','msrzlxaekz','xbufpltpkl']
aux = 0
f = ''

for j in range(len(l1)):
    count = 0
    for i in range(len(txt)):
        if l1[j][i] == txt[i]:
            count+=1
        else:
            continue
    if j == 0:
        aux = count
        f = l1[j]
    else:
        if count > aux:
            aux = count
            f = l1[j]
print(f)










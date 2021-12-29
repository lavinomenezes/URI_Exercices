count, rep = 0, 0
rep = int(input())
while count < rep:
    txt = input()
    X = int(input())
    txt = list(txt)
    txt = [ord(txt[i]) for i in range(len(txt))]
    for i in range(len(txt)):
        aux = txt[i]-X
        if aux < 65:
            aux +=26
        txt[i] = aux
    txt = ''.join([chr(txt[i]) for i in range(len(txt))])
    print(txt)
    count+=1





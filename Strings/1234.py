while True:
    try:
        txt = str(input())
    except EOFError:
        break
    txt2 = ''
    count = 0
    for i in txt:
        if i != ' ':
            if count%2 == 0:
                txt2 += i.upper()
                count += 1
            else:
                txt2 += i.lower()
                count+= 1
        elif i == ' ':
            txt2 += i
    print(txt2)


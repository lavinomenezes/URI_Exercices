joia = list()
while True:
    try:
        aspas = input()
        if aspas not in joia:
            joia.append(aspas)
    except EOFError:
        break
print(len(joia))
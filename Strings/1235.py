"""""
for i, l in enumerate(txt):
    if i < len(txt)/2:
        met1 += l
    elif i >= len(txt)/2:
        met2 += l
"""
livro = list()
count = 0

X = int(input())
while count < X:
    met1 = ''
    met2 = ''
    txt = str(input())
    Y = int((len(txt) / 2))
    for l in range(Y-1,-1,-1):
        met1 += txt[l]
    for l in range(len(txt)-1, Y-1, -1):
        met2 += txt[l]
    livro.append(met1+met2)
    count += 1
for i in livro:
    print(i)




dc = {
    'suco de laranja': 120,
    'morango fresco':85,
    'mamao':85,
    'goiaba vermelha': 70,
    'manga':56,
    'laranja':50,
    'brocolis': 34
}

while True:

    t = int(input())
    if t == 0:
        break
    c = 0
    for i in range(t):
        fruta = input().split()
        qt = int(fruta[0])
        vit = ' '.join(fruta[1:])
        c += dc[vit]*qt
    if c < 110:
        print('Mais',110-c,'mg')
    elif c > 130:
        print('Menos', c-130,'mg')
    else:
        print(c,'mg')
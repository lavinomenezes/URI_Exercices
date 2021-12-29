from re import sub
for i in range(int(input())):
    txt = input()
    txt = txt.lower()
    txt = sub('[^a-z]', '', txt)
    maior = list()
    freq = dict()
    for i, c in enumerate(txt):
        if c in maior:
            continue
        else:
            maior.append(c)
    maior.sort()
    for i in maior:
        freq[i] = txt.count(i)
    grande = max(freq.values())
    for i, c in freq.items():
        if c == grande:
            print(i, end='')
    print()
from collections import Counter
while True:
    try:
        voga = input()
        txt = input()
        count = 0
        d1 = Counter(txt)
        for i in range(len(voga)):
            count += d1[voga[i]]
        print(count)
    except EOFError:
        break
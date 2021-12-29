txt = list()
for i in range(int(input())):
    txt.append(input().split())
for i in txt:
    i.sort(key=len,reverse=True)
for i in txt:
    print(" ".join(i))
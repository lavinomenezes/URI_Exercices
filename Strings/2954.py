from re import sub
for _ in range(int(input())):
    txt = input().lower()
    txt = sub('[^a-zA-Z]', '', txt)
    txt = txt.split("jogo")
    print(len(max(txt))+4)
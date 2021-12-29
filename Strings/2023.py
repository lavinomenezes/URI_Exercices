txt = list()
while True:
    try:
       txt.append(input())
    except EOFError:
        break
txt.sort(key=str.lower)
print(txt[-1])



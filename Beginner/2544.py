from math import log
while True:
    try:
        x = int(input())
        c = log(x,2)
        print(int(c))
    except EOFError:
        break
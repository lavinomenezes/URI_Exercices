while True:
    try:
        X = int(input())
    except EOFError:
        break
    lesmas = map(int,input().split())
    fast = max(lesmas)
    if fast < 10:
        print(1)
    elif fast >= 10 and fast < 20:
        print(2)
    else:
        print(3)

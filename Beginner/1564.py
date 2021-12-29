while True:
    try:
        X = int(input())
    except EOFError:
        break
    if X == 0:
        print("vai ter copa!")
    else:
        print("vai ter duas!")
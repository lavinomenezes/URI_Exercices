while True:
    quad = input().split()
    X = int(quad[0])
    Y = int(quad[1])
    if X == 0 or Y == 0:
        break
    else:
        if X > 0 and Y > 0:
            print("primeiro")
        elif X < 0 and Y > 0:
            print("segundo")
        elif X > 0 and Y < 0:
            print("quarto")
        else:
            print("terceiro")
        continue
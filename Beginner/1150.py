Y, count, pos = 0, 0, 1
X = int(input())
while True:
    Y = int(input())
    if X<Y:
        break
    else:
        continue
count = X
while True:
    count +=1
    X += count
    if X > Y:
        pos += 1
        break
    elif X<Y:
        pos += 1
        continue
print(pos)



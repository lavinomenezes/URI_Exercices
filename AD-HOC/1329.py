from collections import Counter
while True:
    n = int(input())
    if n == 0:
        break
    d1 = Counter([int(x) for x in input().split()])
    print("Mary won " + str(d1[0]) + " times and John won "+str(d1[1])+" times")

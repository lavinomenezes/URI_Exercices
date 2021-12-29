X = int(input())
S = list()
count = 0
while count < X:
    leds = 0
    Y = str(input())
    for n in Y:
        n = int(n)
        if n == 1:
            leds +=2
        elif n == 2 or n == 3 or n == 5:
            leds +=5
        elif n == 4:
            leds +=4
        elif n == 6 or n == 9 or n == 0:
            leds +=6
        elif n == 7:
            leds +=3
        elif n == 8:
            leds +=7
    S.append(leds)
    count+=1
for n in S:
    print(n, "leds")


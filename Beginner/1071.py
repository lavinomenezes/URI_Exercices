IN = 0
OUT = 0
X = int(input())
for i in range(0,X):
    Y = int(input())
    if Y >= 10 and Y <=20:
        IN +=1
    else:
        OUT += 1
print(IN, "in")
print(OUT, "out")
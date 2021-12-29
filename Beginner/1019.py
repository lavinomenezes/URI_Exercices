X = int(input())
HORA = 0
MIN = 0
while X > 60:
    while X >= 3600:
        HORA += 1
        X -= 3600
    while X >= 60:
        MIN += 1
        X -= 60
print('{0}:{1}:{2}'.format(HORA, MIN, X))


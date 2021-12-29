V = input().split()
X = float(V[0])
Y = float(V[1])

if X == 0.0 and Y == 0.0:
    print("Origem")
elif X == 0 and Y != 0:
    print("Eixo Y")
elif X !=0 and Y == 0:
    print("Eixo X")
elif X > 0 and Y > 0:
    print("Q1")
elif X < 0 and Y < 0:
    print("Q3")
elif X > 0 and Y < 0:
    print("Q4")
elif X < 0 and Y > 0:
    print("Q2")
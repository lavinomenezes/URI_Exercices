from decimal import *
X = input().split()
n1 = float(X[0])
n2 = float(X[1])
n3 = float(X[2])
n4 = float(X[3])
media = Decimal((n1*0.2) + (n2*0.3) + (n3*0.4) + (n4*0.1))
print("Media: %.2f" % media)
if media >= 7.0:
    print("Aluno aprovado.")

elif media >= 5.0 and media <= 6.9:
    print("Aluno em exame.")
    E = float(input())
    print("Nota do exame: %.1f" % E)
    exame = Decimal(E) + media
    if exame/2 >= 5.0:
        print("Aluno aprovado.")
    else:
        print('Aluno reprovado.')
    print("Media final:", round(exame/2,1))
else:
    print('Aluno reprovado.')
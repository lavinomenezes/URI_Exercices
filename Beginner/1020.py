X = int(input())
ano = 0
mes = 0
while X >= 365:
    ano += 1
    X -= 365
while X < 365 and X >= 30:
    mes += 1
    X -= 30

print(ano,"ano(s)")
print(mes,"mes(es)")
print(X,"dia(s)")

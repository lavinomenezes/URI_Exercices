from decimal import *
NOME = input()
A = float(input())
B = float(input())
TOTAL = Decimal(A + B*.15)
print("TOTAL = R$", round(TOTAL,2))

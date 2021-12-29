V = input().split('.')
X = int(V[0])
Y = int(V[1])
CEM = 0
CIN = 0
VIN = 0
DEZ = 0
CINQ = 0
DOI = 0
UN = 0
MCIN = 0
MVC = 0
MDEZ = 0
MCINQ = 0
MUN = 0
while X > 0:
    while X >= 100:
        CEM += 1
        X -= 100
    while X < 100 and X >= 50:
        CIN += 1
        X -=50
    while X < 50 and X >= 20:
        VIN +=1
        X -= 20
    while X < 20 and X >= 10:
        DEZ += 1
        X -= 10
    while X < 10 and X >= 5:
            CINQ += 1
            X -=5
    while X < 5 and X >= 2:
            DOI += 1
            X -= 2
    while X < 2 and X >= 1:
            UN += 1
            X -= 1
#MOEDAS
while Y > 0:
    while Y < 100 and Y >= 50:
            MCIN += 1
            Y -= 50
    while Y < 50 and Y >= 25:
            MVC += 1
            Y -= 25
    while Y < 25 and Y >= 10:
            MDEZ += 1
            Y -= 10
    while Y < 10 and Y >= 5:
            MCINQ += 1
            Y -= 5
    while Y < 5 and Y >= 1:
            MUN += 1
            Y -= 1


print("NOTAS:")
print(CEM,"nota(s) de R$ 100.00")
print(CIN,"nota(s) de R$ 50.00")
print(VIN,"nota(s) de R$ 20.00")
print(DEZ,"nota(s) de R$ 10.00")
print(CINQ,"nota(s) de R$ 5.00")
print(DOI,"nota(s) de R$ 2.00")
print("MOEDAS:")
print(UN,"moeda(s) de R$ 1.00")
print(MCIN,"moeda(s) de R$ 0.50")
print(MVC,"moeda(s) de R$ 0.25")
print(MDEZ,"moeda(s) de R$ 0.10")
print(MCINQ,"moeda(s) de R$ 0.05")
print(MUN,"moeda(s) de R$ 0.01")



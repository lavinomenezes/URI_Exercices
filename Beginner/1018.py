X = int(input())
CEM = 0
CIN = 0
VIN = 0
DEZ = 0
CINQ = 0
DOI = 0
UN = 0
print(X)
while X > 0 :
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

print(CEM,"nota(s) de R$ 100,00")
print(CIN,"nota(s) de R$ 50,00")
print(VIN,"nota(s) de R$ 20,00")
print(DEZ,"nota(s) de R$ 10,00")
print(CINQ,"nota(s) de R$ 5,00")
print(DOI,"nota(s) de R$ 2,00")
print(UN,"nota(s) de R$ 1,00")


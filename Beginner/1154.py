from decimal import Decimal
count = 0
total = 0
while True:
    X = int(input())
    if X > 0:
        total += X
        count +=1
        continue
    else:
        break
media = Decimal(total/count)
print("%.2f" % media)
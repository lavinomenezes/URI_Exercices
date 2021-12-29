x , y = input().split()
s = 0
for i in range(int(x)):
    l = input().split()
    if '0' not in l:
        s+=1
print(s)
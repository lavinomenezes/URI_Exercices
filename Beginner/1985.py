p1 = {
    '1001':1.50,
    '1002':2.50,
    '1003':3.50,
    '1004':4.50,
    '1005':5.50,
}
ac = 0
for i in range(int(input())):
    txt, X = input().split()
    ac += p1[txt]*int(X)
print("%.2f" % ac)
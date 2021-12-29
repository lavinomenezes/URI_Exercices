from math import sqrt
X = int(input())
a = sqrt(5)
b = ((1+a)/2)**X
c = ((1-a)/2)**X
n = (b-c)/a
print("%.1f" % n)
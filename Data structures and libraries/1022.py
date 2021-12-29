def MDC_R(a,b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    r = a % b
    return MDC_R(b, r)

for i in range(int(input())):
    l1 = input().split()
    N1 = int(l1[0])
    N2 = int(l1[4])
    D1 = int(l1[2])
    D2 = int(l1[6])
    if l1[3] == '+':
        n = (N1*D2 + N2*D1)
        d = (D1*D2)
        print(str(n)+"/"+str(d),"=",str(int(n / MDC_R(n, d)))+"/"+str(int(d / MDC_R(n, d))))
    elif l1[3] == '-':
        n = (N1*D2 - N2*D1)
        d = (D1*D2)
        print(str(n) + "/" + str(d), "=", str(int(n / MDC_R(abs(n), d))) + "/" + str(int(d / MDC_R(abs(n), d))))
    elif l1[3] == '*':
        n = (N1*N2)
        d = (D1*D2)
        print(str(n) + "/" + str(d), "=", str(int(n / MDC_R(n, d))) + "/" + str(int(d / MDC_R(n, d))))
    elif l1[3] == '/':
        n = (N1*D2)
        d = (N2*D1)
        print(str(n) + "/" + str(d), "=", str(int(n / MDC_R(n, d))) + "/" + str(int(d / MDC_R(n, d))))
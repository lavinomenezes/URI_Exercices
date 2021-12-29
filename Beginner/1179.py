par, imp = list(), list()
for i in range(15):
    X = int(input())
    if X % 2 == 0:
        par.append(X)
    else:
        imp.append(X)
    if len(par) == 5:
        for j, v in enumerate(par):
            print("par[" + str(j) + "] = " + str(v))
        par.clear()
    elif len(imp) == 5:
        for j, v in enumerate(imp):
            print("impar[" + str(j) + "] = " + str(v))
        imp.clear()
if len(imp) !=0:
    for j, v in enumerate(imp):
            print("impar[" + str(j) + "] = " + str(v))
    imp.clear()
if len(par) !=0:
    for j, v in enumerate(par):
        print("par[" + str(j) + "] = " + str(v))
    par.clear()

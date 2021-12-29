count = 0
X = 200
while count<100:
    print("N[" + str(count) + "] = ", end='')
    print("%.4f" % X)
    X = X -(X/2)
    count+=1


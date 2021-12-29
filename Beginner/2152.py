for i in range(int(input())):
    X, Y, Z = input().split()
    if Z == '1':
        print('{:0>2}:{:0>2} - A porta abriu!'.format(X,Y))
    else:
        print('{:0>2}:{:0>2} - A porta fechou!'.format(X,Y))
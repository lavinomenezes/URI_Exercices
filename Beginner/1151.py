fib = ['0','1']
X = int(input())
for i in range(0,X-2):
    som = int(fib[-1]) + int(fib[-2])
    fib.append(str(som))
n1 = ' '.join([i for i in fib])
print(n1)

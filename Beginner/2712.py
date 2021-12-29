import re
rod = {0:'FRIDAY',
       1:'MONDAY',
       2:'MONDAY',
       3:'TUESDAY',
       4:'TUESDAY',
       5:'WEDNESDAY',
       6:'WEDNESDAY',
       7:'THURSDAY',
       8:'THURSDAY',
       9:'FRIDAY',
}
for _ in range(int(input())):
    placa = input().split('-')
    if len(placa[0])!=3 or re.fullmatch('[A-Z]+',placa[0]) == None:
        print('FAILURE')
    elif len(placa[1])!=4 or re.fullmatch('[0-9]+',placa[1]) == None:
        print('FAILURE')
    else:
        print(rod[int(placa[1][-1])])


"""
Soma de Ímpares Consecutivos III
Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir.
Cada caso de teste consiste de dois inteiros X e Y. Você deve apresentar a soma de Y ímpares consecutivos a partir de X
inclusive o próprio X se ele for ímpar. Por exemplo:
para a entrada 4 5, a saída deve ser 45, que é equivalente à: 5 + 7 + 9 + 11 + 13
para a entrada 7 4, a saída deve ser 40, que é equivalente à: 7 + 9 + 11 + 13
"""
count = 0 # inicia váriavel de controle do laço principal
rep = int(input()) # lê o valor indicando quantos casos teste serão gerados
while count < rep: # laço de repetição principal do programa
    soma, imp = 0, 0 #inicia as váriaveis da soma final e quantidade de numeros impares
    X, Y = map(int, input().split()) # lê os valores de X e Y em uma linha e os transforma em inteiros
    while True: # segundo laço de repetição
        if X%2 != 0: # condição para somar apenas numeros impares a partir de X
            soma+=X # incrementa a soma
            imp+=1 # incrementa a quantidade de impares somados
        elif imp == Y: # condição de fizalização do laço
            break
        X += 1 # inclemento do X
    print(soma) # resultado final impresso em tela
    count+=1 # incremento da variavel de controle do laço principal
"""
Soma de Pares Consecutivos
O programa deve ler um valor inteiro X indefinidas vezes. (O programa irá parar quando o valor de X for igual a 0).
Para cada X lido, imprima a soma dos 5 pares consecutivos a partir de X, inclusive o X , se for par.
Se o valor de entrada for 4, por exemplo, a saída deve ser 40, que é o resultado da operação: 4+6+8+10+12,
enquanto que se o valor de entrada for 11, por exempo, a saída deve ser 80, que é a soma de 12+14+16+18+20.
"""
while True: # laço principal
    soma = 0 # inicia variavel que guarda os valores somados
    X = int(input())  # recebe e armazena a vaeriavel X
    if X == 0: # condição de fim do laço
        break
    else:
        for i in range(X,X+10): #Gera os numeros a serem testados
            if i%2 == 0: # condição para checar se o numero é par
                soma += i # incremento com pares
        print(soma) # imprime na tela resultado
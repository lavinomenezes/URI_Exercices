class Pilha:
    def __init__(self):
        self.pilha = []

    def empilhar(self,valor):
        self.pilha.append(valor)

    def desempilhar(self):
        if len(self.pilha) == 0:
            return -1
        else:
            self.pilha.pop()

    def ver_topo(self):
        if len(self.pilha) == 0:
            return -1
        else:
            return self.pilha[len(self.pilha)-1]


for i in range(int(input())):
    p1 = Pilha()
    cont = 0
    diamonds = input()
    for j in diamonds:
        if j == '<':
            p1.empilhar(j)
        if j == '>':
            if p1.ver_topo() == -1:
                pass
            if p1.ver_topo() == '<':
                p1.desempilhar()
                cont+=1

    print(cont)
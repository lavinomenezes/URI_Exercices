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


while True:
    try:
        p1 = Pilha()
        test = 0
        exp = input()
        for i in exp:
            if i == '(':
                p1.empilhar(i)
            if i == ')':
                if p1.ver_topo() == -1:
                    test = -1
                    break
                if p1.ver_topo() == '(' and i == ')':
                    p1.desempilhar()

        if p1.ver_topo() != -1 or test == -1:
            print("incorrect")
        else:
            print("correct")
    except EOFError:
        break
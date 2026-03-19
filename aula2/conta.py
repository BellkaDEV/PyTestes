class Conta:
    def __init__(self, numC, nome, saldo, limiteEspecial):
        self.numC = numC
        self.nome = nome
        self.__saldo = saldo
        self.limiteEspecial = limiteEspecial

    def depositar(self, d):
        self.__saldo += d
    
    def sacar(self, d):
        self.__saldo -= d

    def consultarsaldo(self):
        return self.__saldo
    
    def exibir(self):
        print(f"Codigo: {self.numC}")
        print(f"Nome: {self.nome}")
        print(f"Saldo: R$ {self.numC}")
        print(f"limite Especial: R$ {self.limiteEspecial}")

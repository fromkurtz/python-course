from abc import abstractmethod


class Banco:
    agencia = 9991

    def autenticando(self, cliente):
        if cliente.conta.agencia != self.agencia:
            print('A conta informada nao pertence a esse banco.')
            return
        cliente.conta.permissao = True


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Cliente(Pessoa):
    def __init__(self, nome, idade, conta):
        super().__init__(nome, idade)
        self.nome = nome
        self.idade = idade
        self.conta = conta
    

class Conta:
    def __init__(self, agencia, numero_conta, saldo):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor


    @abstractmethod
    def sacar(self, valor):
        pass


class ContaPoupanca(Conta):
    permissao = False

    def sacar(self, valor):
        if self.saldo - valor < 0 or not self.permissao:
            print('Voce nao tem permissao para sacar')
            return
        self.saldo -= valor



class ContaCorrente(Conta):
    limite = 1000
    permissao = False

    def sacar(self, valor):
        if self.saldo - valor < self.limite * -1 or not self.permissao:
            print('Voce nao tem permissao para sacar')
            return
        self.saldo -= valor

banco = Banco()
conta1 = ContaCorrente(9991, 111111, 1000)
c1 = Cliente('Lisete', 19, conta1)
banco.autenticando(c1)
c1.conta.sacar(500)
print(c1.nome)
print(c1.conta.saldo)
 
print()
 
conta2 = ContaPoupanca(9991, 213333, 300)
c2 = Cliente('João', 32, conta2)
banco.autenticando(c2)
c2.conta.depositar(200)
print(c2.nome)
print(c2.conta.saldo)
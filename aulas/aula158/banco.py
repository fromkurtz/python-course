import contas
import pessoas

class Banco:
    def __init__(
     self,
     agencias: list[int] | None = None,
     clientes: list[pessoas.Pessoaessoa] | None = None,
     contas: list[contas.Conta] | None = None
    ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []


    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            return True
        return False


    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            return True
        return False


    def _checa_conta(self, conta):
        if conta in self.contas:
            return True
        return False
    

    def autenticar(self, ciente, conta):
        
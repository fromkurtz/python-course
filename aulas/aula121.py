# Metodos em instancias de classes Python
# Hard coded - eh algo que foi escrito diretamente no codigo
class Carro:
    def __init__(self, nome='Sei la'):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} esta acelerando...')


fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

corolla = Carro('Corolla')
print(corolla.nome)
corolla.acelerar()
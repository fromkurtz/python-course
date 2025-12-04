class Meta(type):
    def __call__(cls, *args, **kwargs):
        return super().__call__(*args, **kwargs)

class Pessoa(metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        print('NEW e executado')
        return super().__new__(cls)

    def __init__(self, nome):
        print('INIT é executado')
        self.nome = nome

    def __call__(self, x, y):
        print('call chamado', self.nome, x + y)

p1 = Pessoa("João")
print(p1.nome)

class Meta(type):
    pass

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def __call__(self, x, y):
        print('call chamado', self.nome, x + y)

p1 = Pessoa("João")
p1(2, 2)
print(p1.nome)

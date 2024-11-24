import json

CAMINHO_JSON = 'aula126.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('Joao', 33)
p2 = Pessoa('Helena', 12)
p3 = Pessoa('Joana', 53)
bd = [vars(p1), p2.__dict__, vars(p3)]

def fazer_dump():
    with open(CAMINHO_JSON, 'w') as arquivo:
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    print('ELE E O __main__')
    fazer_dump()
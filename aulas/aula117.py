import json

pessoa = {
    'nome': 'Bryan',
    'sobrenome': 'Kurtz Oschoski',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.75,
    'numeros_preferidos': (3, 5, 1, 7, 10),
    'dev': True,
    'nada': None,
}
with open('aula117.json', 'w', encoding='utf8') as arquivo:
    json.dump(
        pessoa,
        arquivo,
        ensure_ascii=False,
        indent=2,
    )
with open('aula117.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    # print(pessoa)
    # print(type(pessoa))
    print(pessoa['nome'])
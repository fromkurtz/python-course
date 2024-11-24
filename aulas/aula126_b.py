#Como você viu na aula anterior, usamos certas convenções para nomes de variáveis, funções, classes e assim por diante. Essas convenções tem um nome que podemos usar para nos referir ao modo como estamos nomeando determinados objetos em nosso programa: PascalCase, camelCase e snake_case.

#PascalCase - significa que todas as palavras iniciam com letra maiúscula e nada é usado para separá-las, como em: MinhaClasse, Classe, MeuObjeto, MeuProgramaMuitoLegal. Essa á a convenção utilizada para classes em Python;

#camelCase - a única diferença de camelCase para PascalCase é a primeira letra. Em camelCase a primeira letra sempre será minúscula e o restante das palavras deverá iniciar com letra maiúscula. Como em: minhaFuncao, funcaoDeSoma, etc... Essa conversão não é usada em Python (apesar de eu confundir as duas e às vezes acabar chamando camelCase de PascalCase ou vice-versa, mas agora você sabe a diferença);

#snake_case - este é o padrão usado em Python para definir qualquer coisa que não for uma classe. Todas as letras serão minúsculas e separadas por um underline, como em: minha_variavel, funcao_legal, soma.

#Os padrões usados em Python são: snake_case para qualquer coisa e PascalCase para classes.


import json

from aula126_a import CAMINHO_JSON, Pessoa

with open(CAMINHO_JSON, 'r') as arquivo:
    pessoas = json.load(arquivo)
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2])

    print(p1.nome, p1.idade)
    print(p2.nome, p2.idade)
    print(p3.nome, p3.idade)


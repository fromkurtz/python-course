# Funcoes decoradoras e decoradores
# Decorar = Adicionar / Remover / Restringir / Alterar
# Funcoes decoradoras sao funcoes que decoream outras funcoes
# Decoradores sao usados para fazer o Python
# usar as funcoes decoradoras em outras funcoes

def criar_funcao(func):
    def interna(*args, **kwargs):
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        return resultado
    return interna

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')

@criar_funcao
def inverte_string(string):
    return string[::-1]



invertida = inverte_string('cabacisse')
print(invertida)
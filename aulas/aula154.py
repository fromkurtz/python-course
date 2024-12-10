# Classes decoradoras (Decorator classes)
class Somar:
    def __init__(self, func):
        self.func = func
        self._multiplicador = 10


    def __call__(self, *args, **kwds):
        resultado = self.func(*args, **kwds)
        
        return resultado * self._multiplicador

@Somar
def soma(x, y):
    return x + y


dois_mais_dois = soma(2, 2)
print(dois_mais_dois)
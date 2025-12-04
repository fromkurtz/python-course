# class Meta(type):
#     def __call__(cls, *args, **kwargs):
#         print('CALL do metaclass é executado')
#         return super().__call__(*args, **kwargs)

# class Pessoa(metaclass=Meta):
#     def __new__(cls, *args, **kwargs):
#         print('NEW e executado')
#         return super().__new__(cls)

#     def __init__(self, nome):
#         print('INIT é executado')
#         self.nome = nome

#     def __call__(self, x, y):
#         print('call chamado', self.nome, x + y)

# p1 = Pessoa("João")
# print(p1.nome)

class Singleton(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class AppSettings(metaclass=Singleton):
    def __init__(self):
        """ O init sera chamado todas as vezes que a classe for instanciada,"""
        self.tema = "O tema escuro"
        self.font = '18px'


if __name__ == "__main__":
    as1 = AppSettings()

    as1.tema = 'outra coisa'

    as2 = AppSettings()
    as3 = AppSettings()

    print(as3.tema)
    print(as1 == as2)
    print(as1 == as3)
    print(as2 == as3)
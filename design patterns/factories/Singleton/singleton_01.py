"""
O Singleton tem a intencao de garantir que uma classe tenha apenas uma instancia
e fornecer um ponto global de acesso a ela.
"""

class AppSettings:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self):
        """ O init sera chamado todas as vezes que a classe for instanciada,"""
        self.tema = "O tema escuro"
        self.font = '18px'


if __name__ == "__main__":
    as1 = AppSettings()
    as1.tema = 'O tema claro'
    print(as1.tema)

    as2 = AppSettings()
    print(as1.tema)
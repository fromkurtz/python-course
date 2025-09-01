from abc import ABC, abstractmethod

class VeiculoLuxo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None:
        pass

class VeiculoPopular(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None:
        pass

class CarroLuxoZN(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print("Buscando cliente de carro de luxo")

class CarroPopularZN(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print("Buscando cliente de carro popular")

class MotoPopularZN(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print("Buscando cliente de Moto")

class CarroLuxoZS(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print("Buscando cliente de carro de luxo")

class CarroPopularZS(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print("Buscando cliente de carro popular")

class MotoPopularZS(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print("Buscando cliente de Moto")

class VeiculoFactory(ABC):
    @staticmethod
    @abstractmethod
    def get_carro_luxo(tipo: str) -> VeiculoLuxo:
        pass
    
    @staticmethod
    @abstractmethod
    def get_carro_popular(tipo: str) -> VeiculoPopular:
        pass

    @staticmethod
    @abstractmethod
    def get_moto_popular(tipo: str) -> VeiculoPopular:
        pass


class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro_luxo(tipo: str) -> VeiculoLuxo:
        return CarroLuxoZN()

    @staticmethod
    def get_carro_popular(tipo: str) -> VeiculoPopular:
        return CarroPopularZN()

    @staticmethod
    def get_moto_popular(tipo: str) -> VeiculoPopular:
        return MotoPopularZN()
        

class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro_luxo(tipo: str) -> VeiculoLuxo:
        return CarroLuxoZS()

    @staticmethod
    def get_carro_popular(tipo: str) -> VeiculoPopular:
        return CarroPopularZS()

    @staticmethod
    def get_moto_popular(tipo: str) -> VeiculoPopular:
        return MotoPopularZS()
    
class Cliente:
    def busca_clientes(self):
        for factory in [ZonaNorteVeiculoFactory(), ZonaSulVeiculoFactory()]:
            carro_popular = factory.get_carro_popular("popular")
            carro_popular.buscar_cliente()

            carro_luxo = factory.get_carro_luxo("luxo")
            carro_luxo.buscar_cliente()

            moto_popular = factory.get_moto_popular("moto")
            moto_popular.buscar_cliente()

if __name__ == "__main__":
    cliente = Cliente()
    cliente.busca_clientes()

"""
Na programação POO, o termo factory (fábrica) refere-se a uma classe ou método
que é responsável por criar objetos.

Vantagens:
    Permitem criar um sistema com baixo acoplamento entre classes porque
    ocultam as classes que criam os objetos do código cliente.

    Facilitam a adição de novas classes ao código, porque o cliente não
    conhece e nem utiliza a implementação da classe (utiliza a factory).

    Podem facilitar o processo de "cache" ou criação de "singletons" porque a
    fábrica pode retornar um objeto já criado para o cliente, ao invés de criar
    novos objetos sempre que o cliente precisar.

Desvantagens:
    Podem introduzir muitas classes no código

Vamos ver 2 tipos de Factory da GoF: Factory method e Abstract Factory

Nessa aula:
Simple Factory <- Uma espécie de Factory Method parametrizado
Simple Factory pode não ser considerado um padrão de projeto por si só
Simple Factory pode quebrar princípios do SOLID
"""

from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None:
        pass

class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print("Buscando cliente de carro de luxo")

class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print("Buscando cliente de carro popular")

class Moto(Veiculo):
    def buscar_cliente(self) -> None:
        print("Buscando cliente de Moto")

class VeiculoFactory(ABC):
    def __init__(self, tipo):
        self.carro = self.get _carro(tipo)

    @staticmethod
    @abstractmethod
    def get_carro(tipo: str) -> Veiculo:
        pass

    def buscar_cliente(self):
        self.carro.buscar_cliente()

class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == "luxo":
            return CarroLuxo()
        elif tipo == "popular":
            return CarroPopular()
        elif tipo == "moto":
            return Moto()
        else:
            raise ValueError(f"Tipo de carro '{tipo}' não reconhecido")
        

class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        
        if tipo == "popular":
            return CarroPopular()
        else:
            raise ValueError(f"Tipo de carro '{tipo}' não reconhecido")

if __name__ == "__main__":
    from random import choice
    veiculos_disponiveis_zona_norte = ["luxo", "popular", "moto"]
    veiculos_disponiveis_zona_sul = ["popular"]

    print("Zona Norte")
    for i in range(10):
        carro = ZonaNorteVeiculoFactory(choice(veiculos_disponiveis_zona_norte))
        carro.buscar_cliente()

    print()

    print("Zona Sul")
    for i in range(10):
        carro2 = ZonaSulVeiculoFactory(choice(veiculos_disponiveis_zona_sul))
        carro2.buscar_cliente()
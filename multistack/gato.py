from animal import Animal
from interface_animal import InterfaceAnimeal

class Gato(Animal, InterfaceAnimeal):
    def __init__(self, nome, idade, cor, qtd_bonilhas) -> None:
        super().__init__(nome, idade, cor)
        self.__qtd_bonilhas = qtd_bonilhas

    @property
    def qtd_bonilhas(self):
        return self.qtd_bonilhas
    
    @qtd_bonilhas.setter
    def qtd_brinquedo(self, qtd_bonilhas):
         self.qtd_bonilhas = qtd_bonilhas

    def miar(self):
        return "miau"

    def fazer_barulho(self):
        return "miau"

    def brincar(self):
        pass

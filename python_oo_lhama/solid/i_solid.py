
#EXEMPLO RUIM QUE QUEBRA O I DE SOLID

from abc import ABC, abstractmethod

class Trabalhador(ABC):
    @abstractmethod
    def trabalhar(self):
        pass

    @abstractmethod
    def comer(self):
        pass



class Humano(Trabalhador):
    def trabalhar(self):
        print("Humano está trabalhando")

    def comer(self):
        print("Humano está comendo")

class Robô(Trabalhador):
    def trabalhar(self):
        print("Robô está trabalhando")

    def comer(self):
        raise NotImplementedError("Robôs não comem")


#EXEMPLO CORRETO QUE RESPEITA O I DE SOLID

class Trabalhador(ABC):
    @abstractmethod
    def trabalhar(self):
        pass

class Comedor(ABC):
    @abstractmethod
    def comer(self):
        pass


class Humano(Trabalhador, Comedor):
    def trabalhar(self):
        print("Humano está trabalhando")

    def comer(self):
        print("Humano está comendo")

class Robo(Trabalhador):
    def trabalhar(self):
        print("Robô está trabalhando")

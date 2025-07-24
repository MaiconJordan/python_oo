from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def desenhar(self):
        pass

class Circulo(Forma):
    def desenhar(self):
        print("Desenhando círculo")

class Quadrado(Forma):
    def desenhar(self):
        print("Desenhando quadrado")



class Desenhista:
    def desenhar_forma(self, forma):
        forma.desenhar()


desenhista = Desenhista()
desenhista.desenhar_forma(Circulo())
desenhista.desenhar_forma(Quadrado())
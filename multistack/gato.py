from animal import Animal

class Gato(Animal):
    def __init__(self, nome, idade, cor) -> None:
        super().__init__(nome, idade, cor)

    def miar(self):
        return "miau"
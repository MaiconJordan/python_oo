class Mamifero:
    def __init__(self, nome):
        self.nome = nome

    def amamentar(self):
        print(f"{self.nome} está amamentando.")

class Cachorro(Mamifero):
    def __init__(self, nome, raca):
        super().__init__(nome)
        

    def latir(self):
        print(f"{self.nome} está latindo.")

class Gato(Mamifero):
    def __init__(self, nome, cor):
        super().__init__(nome)
        self.cor = cor

    def miar(self):
        print(f"{self.nome} está miando.")

dog = Cachorro("Rex", "Labrador")
dog.amamentar()
dog.latir()

cat = Gato("Miau", "Preto")
cat.amamentar()
cat.miar()
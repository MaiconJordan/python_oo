class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}.")
        self.__mostrar_segredo()

    def __mostrar_segredo(self):
        print("Este é um método privado!")

p = Pessoa("Maicon")
p.apresentar()

# O código abaixo geraria erro, pois __mostrar_segredo é privado:
# p.__mostrar_segredo()
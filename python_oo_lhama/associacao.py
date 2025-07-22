class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.escola = None  # Associação com Escola (ainda vazia)

    def set_escola(self, escola):
        self.escola = escola

    def mostrar_dados(self):
        if self.escola:
            print(f"{self.nome} estuda na escola {self.escola.nome}")
        else:
            print(f"{self.nome} ainda não está matriculado.")


class Escola:
    def __init__(self, nome):
        self.nome = nome



escola = Escola("Escola Python Pro")
aluno = Aluno("Maicon Rocha")

# Fazendo a associação
aluno.set_escola(escola)

# Exibindo dados
aluno.mostrar_dados()


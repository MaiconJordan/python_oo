class Usuario:
    # Variável de classe para contar o número de usuários criados
    total_usuarios = 0

    def __init__(self, nome):
        self.nome = nome
        Usuario.total_usuarios += 1

    @classmethod
    def obter_total_usuarios(cls):
        return cls.total_usuarios

# Exemplo de uso em um sistema de cadastro de usuários
u1 = Usuario("Alice")
u2 = Usuario("Bob")
u3 = Usuario("Carol")

print(f"Total de usuários cadastrados: {Usuario.obter_total_usuarios()}")
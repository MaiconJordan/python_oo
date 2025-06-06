class Contador:
    total = 0  # atributo estático

    def __init__(self):
        Contador.total += 1

# Exemplo de uso
a = Contador()
b = Contador()
c = Contador()

print(Contador.total)  # Saída: 3
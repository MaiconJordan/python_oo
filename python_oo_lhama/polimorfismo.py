class Funcionario:
    def calcular_pagamento(self):
        raise NotImplementedError("Subclasse deve implementar este método")

class FuncionarioCLT(Funcionario):
    def __init__(self, salario_mensal):
        self.salario_mensal = salario_mensal

    def calcular_pagamento(self):
        return self.salario_mensal

class FuncionarioPJ(Funcionario):
    def __init__(self, horas_trabalhadas, valor_hora):
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def calcular_pagamento(self):
        return self.horas_trabalhadas * self.valor_hora

def processar_pagamentos(funcionarios):
    for funcionario in funcionarios:
        print(f'Pagamento: R$ {funcionario.calcular_pagamento():.2f}')

# Exemplo de uso
funcionarios = [
    FuncionarioCLT(3000),
    FuncionarioPJ(160, 25)
]

processar_pagamentos(funcionarios)
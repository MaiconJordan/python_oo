# Princípio da Responsabilidade Única (Single Responsibility Principle - SRP)
# Cada classe deve ter apenas uma razão para mudar, ou seja, deve ter apenas uma responsabilidade.

class GeradorDeRelatorio:
    """
    Responsável apenas por gerar o conteúdo do relatório.
    """
    def __init__(self, dados):
        self.dados = dados

    def gerar_relatorio(self):
        # Gera o relatório a partir dos dados
        relatorio = "Relatório de Vendas\n"
        for item in self.dados:
            relatorio += f"{item['produto']}: {item['quantidade']} unidades vendidas\n"
        return relatorio

class ImpressoraDeRelatorio:
    """
    Responsável apenas por imprimir o relatório.
    """
    def imprimir(self, relatorio):
        print(relatorio)

# Exemplo de uso:
dados = [
    {"produto": "Caneta", "quantidade": 10},
    {"produto": "Lápis", "quantidade": 20}
]

gerador = GeradorDeRelatorio(dados)
relatorio = gerador.gerar_relatorio()

impressora = ImpressoraDeRelatorio()
impressora.imprimir(relatorio)
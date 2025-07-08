class Nodo:
    def __init__(self, sigla, nomeEstado):
        self.sigla = sigla
        self.nomeEstado = nomeEstado
        self.proximo = None

class TabelaHash:
    def __init__(self):
        self.tabela = [None] * 10
    
    def funcao_hash(self, sigla):
        if sigla == "DF":
            return 7
        else:
            ascii1 = ord(sigla[0])
            ascii2 = ord(sigla[1])
            return (ascii1 + ascii2) % 10
    
    def inserir_inicio(self, posicao, nodo):
        if self.tabela[posicao] is None:
            self.tabela[posicao] = nodo
        else:
            nodo.proximo = self.tabela[posicao]
            self.tabela[posicao] = nodo
    
    def inserir_estado(self, sigla, nomeEstado):
        posicao = self.funcao_hash(sigla)
        nodo = Nodo(sigla, nomeEstado)
        self.inserir_inicio(posicao, nodo)
    
    def imprimir_tabela(self):
        print("=== TABELA HASH ===")
        for i in range(10):
            print(f"Posição {i}: ", end="")
            if self.tabela[i] is None:
                print("Vazia")
            else:
                atual = self.tabela[i]
                siglas = []
                while atual is not None:
                    siglas.append(atual.sigla)
                    atual = atual.proximo
                print(" -> ".join(siglas))
        print()

if __name__ == "__main__":
    tabela = TabelaHash()
    
    print("TABELA HASH ANTES DE INSERIR QUALQUER INFORMAÇÃO:")
    tabela.imprimir_tabela()
    
    estados = [
        ("AC", "Acre"),
        ("AL", "Alagoas"),
        ("AP", "Amapá"),
        ("AM", "Amazonas"),
        ("BA", "Bahia"),
        ("CE", "Ceará"),
        ("DF", "Distrito Federal"),
        ("ES", "Espírito Santo"),
        ("GO", "Goiás"),
        ("MA", "Maranhão"),
        ("MT", "Mato Grosso"),
        ("MS", "Mato Grosso do Sul"),
        ("MG", "Minas Gerais"),
        ("PA", "Pará"),
        ("PB", "Paraíba"),
        ("PR", "Paraná"),
        ("PE", "Pernambuco"),
        ("PI", "Piauí"),
        ("RJ", "Rio de Janeiro"),
        ("RN", "Rio Grande do Norte"),
        ("RS", "Rio Grande do Sul"),
        ("RO", "Rondônia"),
        ("RR", "Roraima"),
        ("SC", "Santa Catarina"),
        ("SP", "São Paulo"),
        ("SE", "Sergipe"),
        ("TO", "Tocantins")
    ]
    
    for sigla, nome in estados:
        tabela.inserir_estado(sigla, nome)
    
    print("TABELA HASH APÓS INSERIR OS 26 ESTADOS E O DISTRITO FEDERAL:")
    tabela.imprimir_tabela()
    
    tabela.inserir_estado("MJ", "Maicon Jordan")
    
    print("TABELA HASH APÓS INSERIR OS 26 ESTADOS, DF E O ESTADO FICTÍCIO:")
    tabela.imprimir_tabela()
    
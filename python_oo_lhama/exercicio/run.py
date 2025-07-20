class Loja:

    valor_taxa = 1.10

    def __init__(self, valor_produto_buto: float) -> None:
        self.valor_produto_buto = valor_produto_buto

    def consultar_valor_produto(self) -> float:
        return self.valor_produto_buto * self.valor_taxa
    
    @classmethod
    def alterar_taxa(cls, nova_taxa: float) -> None:
        cls.valor_taxa = nova_taxa

loja = Loja(100.0)
print(f"Valor do produto com taxa: {loja.consultar_valor_produto()}")
Loja.alterar_taxa(1.20)
print(f"Valor do produto com nova taxa: {loja.consultar_valor_produto()}")
loja2 = Loja(200.0)
print(f"Valor do produto na segunda loja com taxa: {loja2.consultar_valor_produto()}")
Loja.alterar_taxa(1.30)     
print(f"Valor do produto na segunda loja com nova taxa: {loja2.consultar_valor_produto()}")

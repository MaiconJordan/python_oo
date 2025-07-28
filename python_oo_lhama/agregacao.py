class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def informacoes_do_produto(self):
        print(f"Produto: {self.nome} | Valor: R${self.valor:.2f}")

class CarrinhoDeCompras:
    def __init__(self, produtos=None):
        if produtos is None:
            self.produtos = []
        else:
            self.produtos = produtos

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def mostrar_produtos(self):
        print("Produtos no carrinho:")
        for produto in self.produtos:
            produto.informacoes_do_produto()

    def total(self):
        return sum(produto.valor for produto in self.produtos)

# Exemplo de uso:
p1 = Produto("Notebook", 3500.00)
p2 = Produto("Mouse", 150.00)
p3 = Produto("Teclado", 200.00)

carrinho = CarrinhoDeCompras([p1, p2])
carrinho.adicionar_produto(p3)

carrinho.mostrar_produtos()
print(f"Total da compra: R${carrinho.total():.2f}")
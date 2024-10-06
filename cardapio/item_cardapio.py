from abc import ABC, classmethod


class ItemCardapio(ABC): 
    
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

@classmethod
def aplicar_desconto(self):
    pass
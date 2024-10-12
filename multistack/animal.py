class Animal:
    def __init__(self, nome, idade, cor):
        self._nome = nome
        self._idade = idade
        self._cor = cor

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
         self._nome = nome

    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, idade):
         self._idade = idade

    @property
    def cor(self):
        return self._cor
    
    @cor.setter
    def qtd_brinquedo(self, cor):
         self._cor = cor
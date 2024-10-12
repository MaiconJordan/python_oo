from animal import Animal

class Cachorro(Animal):
    def __init__(self, nome, idade, cor, qtd_brinquedo):
        super().__init__(nome, idade, cor)
        self.__qtd_brinquedo = qtd_brinquedo

    @property
    def qtd_brinquedo(self):
        return self.__qtd_brinquedo
    
    @qtd_brinquedo.setter
    def qtd_brinquedo(self, qtd_brinquedo):
         self.__qtd_brinquedo = qtd_brinquedo

    def latir(self):
        return "au au"
    

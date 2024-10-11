from animal import Animal

class Cachorro(Animal):
    def __init__(self, nome, idade, cor):
        super().__init__(nome, idade, cor)

    def latir(self):
        return "au au"
    

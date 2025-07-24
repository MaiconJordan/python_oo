class Ave:
    def voar(self):
        print("Voando...")

class Andorinha(Ave):
    def voar(self):
        print("Andorinha voando rápido!")

def fazer_ave_voar(ave: Ave):
    ave.voar()

andorinha = Andorinha()
fazer_ave_voar(andorinha)  # funciona perfeitamente!

class Motor:
    def ligar(self):
        print("Motor ligado.")

class Carro:
    def __init__(self, motor):
        self.motor = motor

    def ligar(self):
        self.motor.ligar()
        print("Carro pronto para andar.")

# Injeção de dependência: passamos o motor ao criar o carro
motor = Motor()
carro = Carro(motor)
carro.ligar()
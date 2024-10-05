from Restaurante import Restaurante

restaurante_praca = Restaurante('Nome', 'teste')
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Gui', 5)
restaurante_praca.receber_avaliacao('Gui', 5)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
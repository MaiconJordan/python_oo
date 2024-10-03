from Restaurante import Restaurante

restaurante = Restaurante('Nome', 'teste')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
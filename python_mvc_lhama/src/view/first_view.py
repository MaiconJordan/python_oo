def introduction_page():
    message = '''
            Sistema cadastral
            1 - Cadastrar cliente
            2 - Listar clientes
            3 - Sair
'''
    print(message)
    command = input("Escolha uma opção: ")
    return command
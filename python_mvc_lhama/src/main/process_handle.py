from .constructor.introduction_process import introduction_process

def start():
    while True:
        command = introduction_process()
        if command == '1':
            print("Cadastrar cliente")
            # Logic for registering a client would go here
        elif command == '2':
            print("Listar clientes")
            # Logic for listing clients would go here
        elif command == '3':
            exit()
        else:
            print("Opção inválida, tente novamente.")
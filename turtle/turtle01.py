

def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ")
    while True:
        email = input("Digite o email do usuário: ")
        if "@" not in email:
            print("Email inválido! O email deve conter '@'.")
        else:
            break
    senha = input("Digite a senha do usuário: ")

    with open("usuarios.txt", "a") as arquivo:
        arquivo.write(f"{nome},{email},{senha}\n")
    print("Usuário cadastrado com sucesso!\n")

def listar_usuarios():
    print("\nUsuários cadastrados:")
    try:
        with open("usuarios.txt", "r") as arquivo:
            for linha in arquivo:
                nome, email, _ = linha.strip().split(",")
                print(f"Nome: {nome}, Email: {email}")
    except FileNotFoundError:
        print("Nenhum usuário cadastrado ainda.\n")

def menu():
    while True:
        print("1 - Cadastrar usuário")
        print("2 - Listar usuários")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            break
        else:
            print("Opção inválida!\n")

if __name__ == "__main__":
    menu()